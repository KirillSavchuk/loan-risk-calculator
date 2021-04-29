import json
from typing import List

from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView

from .models import *
from .service import config_importer


def get_loan_count_by_status(status: RiskCalculationStatus) -> int:
    return Loan.objects.filter(risk_calculation_status=status).count()


class LoanListView(ListView):
    model = Loan

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total'] = Loan.objects.count()
        context['status'] = dict()
        context['status']['match'] = get_loan_count_by_status(RiskCalculationStatus.MATCH)
        context['status']['exception'] = get_loan_count_by_status(RiskCalculationStatus.EXCEPTION)
        context['status']['error'] = get_loan_count_by_status(RiskCalculationStatus.ERROR)
        return context


def loan_refresh(request):
    loans: List[Loan] = Loan.objects.all()
    for loan in loans:
        loan.save()
    return HttpResponse(f"Refreshed {loans.count()} loans.")


def import_loan_config(request):
    file_names_str = request.GET.get('files')
    if not file_names_str:
        return HttpResponseNotFound("Please provide query parameters: and 'files'.")

    file_names: list = file_names_str.split(',')
    imported_files: list = config_importer.import_loan_config(file_names=file_names)

    return HttpResponse(json.dumps(imported_files))
