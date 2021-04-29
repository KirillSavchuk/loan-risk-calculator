from import_export import resources

from .models import Loan


class LoanResource(resources.ModelResource):
    class Meta:
        model = Loan
        fields = ('id', 'age', 'monthly_income', 'monthly_expenses', 'free_money', 'dependents', 'external_liabilities',
                  'finished_loans', 'prev_loan_interaction', 'last_status', 'debt_days')
