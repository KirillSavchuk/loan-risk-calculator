from . import models

from rest_framework import serializers


class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Loan
        fields = (
            'id',
            'age', 
            'income', 
            'monthly_expenses', 
            'dependents', 
            'credits', 
            'finished_loans', 
            'last_contact_status', 
            'risk_score', 
        )


