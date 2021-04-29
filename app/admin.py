from django import forms
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *
# Forms
from .resources import LoanResource


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'


class LoanConfigForm(forms.ModelForm):
    class Meta:
        model = LoanConfig
        fields = '__all__'


class LoanAgeConfigForm(forms.ModelForm):
    class Meta:
        model = LoanAgeConfig
        fields = '__all__'


class LoanMonthlyIncomeConfigForm(forms.ModelForm):
    class Meta:
        model = LoanMonthlyIncomeConfig
        fields = '__all__'


class LoanMonthlyExpensesConfigForm(forms.ModelForm):
    class Meta:
        model = LoanMonthlyExpensesConfig
        fields = '__all__'


class LoanFreeMoneyConfigForm(forms.ModelForm):
    class Meta:
        model = LoanFreeMoneyConfig
        fields = '__all__'


class LoanDependentsConfigForm(forms.ModelForm):
    class Meta:
        model = LoanDependentsConfig
        fields = '__all__'


class LoanExternalLiabilitiesConfigForm(forms.ModelForm):
    class Meta:
        model = LoanExternalLiabilitiesConfig
        fields = '__all__'


class LoanFinishedLoansConfigForm(forms.ModelForm):
    class Meta:
        model = LoanFinishedLoansConfig
        fields = '__all__'


class LoanPrevLoanInteractionConfigForm(forms.ModelForm):
    class Meta:
        model = LoanPrevLoanInteractionConfig
        fields = '__all__'


class LoanLastContractStatusConfigForm(forms.ModelForm):
    class Meta:
        model = LoanLastContractStatusConfig
        fields = '__all__'


# Admins


class LoanAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = LoanForm
    ordering = ('id', 'age', 'last_status')
    list_display = ['id', 'age', 'monthly_income', 'monthly_expenses', 'free_money', 'dependents',
                    'external_liabilities', 'finished_loans', 'last_status', 'debt_days', 'is_bad_loan',
                    'risk_score', 'will_be_bad_loan', 'risk_calculation_status']
    readonly_fields = ['id', 'is_bad_loan', 'risk_score', 'will_be_bad_loan', 'risk_calculation_status']
    resource_class = LoanResource


class LoanConfigAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = LoanConfigForm
    list_display = ['max_debt_days', 'min_risk_score']


class LoanAgeConfigAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = LoanAgeConfigForm
    list_display = ['upper_value', 'weight']


class LoanMonthlyIncomeConfigAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = LoanMonthlyIncomeConfigForm
    list_display = ['upper_value', 'weight']


class LoanMonthlyExpensesConfigAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = LoanMonthlyExpensesConfigForm
    list_display = ['upper_value', 'weight']


class LoanFreeMoneyConfigAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = LoanFreeMoneyConfigForm
    list_display = ['upper_value', 'weight']


class LoanDependentsConfigAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = LoanDependentsConfigForm
    list_display = ['value', 'weight']


class LoanExternalLiabilitiesConfigAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = LoanExternalLiabilitiesConfigForm
    list_display = ['upper_value', 'weight']


class LoanFinishedLoansConfigAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = LoanFinishedLoansConfigForm
    list_display = ['upper_value', 'weight']


class LoanPrevLoanInteractionConfigAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = LoanPrevLoanInteractionConfigForm
    list_display = ['value', 'weight']


class LoanLastContractStatusConfigAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = LoanLastContractStatusConfigForm
    list_display = ['value', 'weight']


admin.site.register(Loan, LoanAdmin)
admin.site.register(LoanConfig, LoanConfigAdmin)
admin.site.register(LoanAgeConfig, LoanAgeConfigAdmin)
admin.site.register(LoanMonthlyIncomeConfig, LoanMonthlyIncomeConfigAdmin)
admin.site.register(LoanMonthlyExpensesConfig, LoanMonthlyExpensesConfigAdmin)
admin.site.register(LoanFreeMoneyConfig, LoanFreeMoneyConfigAdmin)
admin.site.register(LoanDependentsConfig, LoanDependentsConfigAdmin)
admin.site.register(LoanExternalLiabilitiesConfig, LoanExternalLiabilitiesConfigAdmin)
admin.site.register(LoanFinishedLoansConfig, LoanFinishedLoansConfigAdmin)
admin.site.register(LoanPrevLoanInteractionConfig, LoanPrevLoanInteractionConfigAdmin)
admin.site.register(LoanLastContractStatusConfig, LoanLastContractStatusConfigAdmin)
