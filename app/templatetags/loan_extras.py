from django import template
from django.template import Library

from app.enums import RiskCalculationStatus

register: Library = template.Library()


@register.simple_tag
def loan_debt_days_class(is_bad_loan: bool) -> str:
    return 'loan-score__bad' if is_bad_loan else ''


@register.simple_tag
def loan_risk_score_class(will_be_bad_loan: bool) -> str:
    return 'loan-score__bad' if will_be_bad_loan else ''


@register.simple_tag
def loan_risk_calculation_status_class(loan_risk_calculation_status: RiskCalculationStatus):
    if loan_risk_calculation_status == RiskCalculationStatus.MATCH:
        return 'table-success'
    elif loan_risk_calculation_status == RiskCalculationStatus.EXCEPTION:
        return 'table-warning'
    elif loan_risk_calculation_status == RiskCalculationStatus.ERROR:
        return 'table-danger'
    else:
        return 'table-light'
