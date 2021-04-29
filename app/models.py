from django.db import models as models

from app.constants import *
from app.enums import RiskCalculationStatus


class LoanConfig(models.Model):
    id = models.AutoField(ID, primary_key=True, serialize=False)
    max_debt_days = models.PositiveIntegerField(CONFIG_MAX_DEBT_DAYS)
    min_risk_score = models.FloatField(CONFIG_MIN_RISK_SCORE)


class LoanAgeConfig(models.Model):
    id = models.AutoField(ID, primary_key=True, serialize=False)
    upper_value = models.PositiveIntegerField(UPPER_VALUE)
    weight = models.FloatField(WEIGHT, default=0.5)


class LoanMonthlyIncomeConfig(models.Model):
    id = models.AutoField(ID, primary_key=True, serialize=False)
    upper_value = models.PositiveIntegerField(UPPER_VALUE)
    weight = models.FloatField(WEIGHT, default=0.5)


class LoanMonthlyExpensesConfig(models.Model):
    id = models.AutoField(ID, primary_key=True, serialize=False)
    upper_value = models.PositiveIntegerField(UPPER_VALUE)
    weight = models.FloatField(WEIGHT, default=0.5)


class LoanFreeMoneyConfig(models.Model):
    id = models.AutoField(ID, primary_key=True, serialize=False)
    upper_value = models.PositiveIntegerField(UPPER_VALUE)
    weight = models.FloatField(WEIGHT, default=0.5)


class LoanDependentsConfig(models.Model):
    id = models.AutoField(ID, primary_key=True, serialize=False)
    value = models.PositiveIntegerField(VALUE)
    weight = models.FloatField(WEIGHT, default=0.5)


class LoanExternalLiabilitiesConfig(models.Model):
    id = models.AutoField(ID, primary_key=True, serialize=False)
    upper_value = models.PositiveIntegerField(UPPER_VALUE)
    weight = models.FloatField(WEIGHT, default=0.5)


class LoanFinishedLoansConfig(models.Model):
    id = models.AutoField(ID, primary_key=True, serialize=False)
    upper_value = models.PositiveIntegerField(UPPER_VALUE)
    weight = models.FloatField(WEIGHT, default=0.5)


class LoanPrevLoanInteractionConfig(models.Model):
    id = models.AutoField(ID, primary_key=True, serialize=False)
    value = models.PositiveIntegerField(VALUE)
    weight = models.FloatField(WEIGHT, default=0.5)


class LoanLastContractStatusConfig(models.Model):
    id = models.AutoField(ID, primary_key=True, serialize=False)
    value = models.PositiveIntegerField(VALUE)
    weight = models.FloatField(WEIGHT, default=0.5)


def get_upper_value_weight(config_class, value) -> float:
    config_obj: config_class = config_class.objects.filter(upper_value__gte=value).order_by('upper_value').first()
    if config_obj:
        return config_obj.weight
    else:
        raise Exception(f"Provided value '{value}' is too large for '{config_class.__name__}' configuration.")


def get_constant_value_weight(config_class, value) -> float:
    config_obj: config_class = config_class.objects.filter(value=value).first()
    if config_obj:
        return config_obj.weight
    else:
        raise Exception(f"Provided value '{value}' was not found in '{config_class.__name__}' configuration.")


class Loan(models.Model):
    id = models.AutoField(ID, primary_key=True, serialize=False)
    age = models.PositiveIntegerField(AGE)
    monthly_income = models.PositiveIntegerField(MONTHLY_INCOME)
    monthly_expenses = models.PositiveIntegerField(MONTHLY_EXPENSES)
    free_money = models.FloatField(FREE_MONEY)
    dependents = models.PositiveIntegerField(DEPENDENTS)
    external_liabilities = models.PositiveIntegerField(EXTERNAL_LIABILITIES)
    finished_loans = models.PositiveIntegerField(FINISHED_LOANS)
    prev_loan_interaction = models.PositiveIntegerField(PREV_LOAN_INTERACTION)
    last_status = models.PositiveIntegerField(LAST_CONTRACT_STATUS)
    debt_days = models.IntegerField(DEBT_DAYS)
    is_bad_loan = models.BooleanField(IS_BAD_LOAN, editable=False)
    risk_score = models.FloatField(RISK_SCORE, editable=False)
    will_be_bad_loan = models.BooleanField(WILL_BE_BAD_LOAN, editable=False)
    risk_calculation_status = models.CharField(
        RISK_CALCULATION_STATUS, editable=False, max_length=32,
        choices=RiskCalculationStatus.ENUM,
        default=RiskCalculationStatus.MATCH
    )

    def save(self, *args, **kwargs):
        self.free_money = round(self.free_money, 2)

        config: LoanConfig = LoanConfig.objects.first()
        self.is_bad_loan = self.calculate_is_bad_loan(config=config)
        self.risk_score = self.calculate_risk_score()
        self.will_be_bad_loan = self.calculate_will_be_bad_loan(config=config)
        self.risk_calculation_status = self.calculate_risk_calculation_status()
        super(Loan, self).save(*args, **kwargs)

    def calculate_is_bad_loan(self, config: LoanConfig) -> bool:
        return self.debt_days >= config.max_debt_days

    def calculate_risk_score(self) -> float:
        age_weight: float = get_upper_value_weight(LoanAgeConfig, self.age)
        monthly_income_weight: float = get_upper_value_weight(LoanMonthlyIncomeConfig, self.monthly_income)
        monthly_expenses_weight: float = get_upper_value_weight(LoanMonthlyExpensesConfig, self.monthly_expenses)
        free_money_weight: float = get_upper_value_weight(LoanFreeMoneyConfig, self.free_money)
        dependents_weight: float = get_constant_value_weight(LoanDependentsConfig, self.dependents)
        external_liabilities_weight: float = get_upper_value_weight(LoanExternalLiabilitiesConfig, self.external_liabilities)
        finished_loans_weight: float = get_upper_value_weight(LoanFinishedLoansConfig, self.finished_loans)
        prev_loan_interaction_weight: float = get_constant_value_weight(LoanPrevLoanInteractionConfig, self.prev_loan_interaction)
        last_status_weight: float = get_constant_value_weight(LoanLastContractStatusConfig, self.last_status)
        risk_score: float = age_weight + monthly_income_weight + monthly_expenses_weight + free_money_weight + dependents_weight + external_liabilities_weight \
                            + finished_loans_weight + prev_loan_interaction_weight + last_status_weight
        return round(risk_score, 2)

    def calculate_will_be_bad_loan(self, config: LoanConfig) -> bool:
        return self.risk_score <= config.min_risk_score

    def calculate_risk_calculation_status(self) -> RiskCalculationStatus:
        if self.is_bad_loan == self.will_be_bad_loan:
            return RiskCalculationStatus.MATCH
        elif not self.is_bad_loan and self.will_be_bad_loan:
            return RiskCalculationStatus.ERROR
        else:
            return RiskCalculationStatus.EXCEPTION
