import os
import sys

import tablib
from import_export import resources
from import_export.resources import Resource
from tablib import Dataset

from app.models import *

loan_configs: list = [
    ('config', LoanConfig),
    ('age', LoanAgeConfig),
    ('dependents', LoanDependentsConfig),
    ('monthly-expense', LoanMonthlyExpensesConfig),
    ('monthly-income', LoanMonthlyIncomeConfig),
    ('monthly-expenses', LoanMonthlyExpensesConfig),
    ('free-money', LoanFreeMoneyConfig),
    ('external-liabilities', LoanExternalLiabilitiesConfig),
    ('finished-loans', LoanFinishedLoansConfig),
    ('prev-loan-interaction', LoanPrevLoanInteractionConfig),
    ('last-contract-status', LoanLastContractStatusConfig),
]

loan_config_files: list = [entry[0] for entry in loan_configs]


def import_loan_config(file_names: list):
    for file_name in file_names:
        if file_name in loan_config_files:
            model_class = [entry[1] for entry in loan_configs if entry[0] == file_name][0]
            try:
                print(f"Trying to import '{file_name}' file into '{model_class.__name__}' model.")
                import_object(model_class, file_name=file_name)
            except Exception as ex:
                print(ex)
    return file_names


def import_object(model_class, file_name: str):
    model_class.objects.all().delete()
    resource: Resource = resources.modelresource_factory(model=model_class)()
    dataset: Dataset = read_xlsx(path=sys.path[0], file_name=file_name)
    resource.import_data(dataset, raise_errors=True, collect_failed_rows=True)


def read_xlsx(path: str, file_name: str):
    dataset: Dataset = tablib.Dataset()
    dataset.xlsx = open(os.path.join(path, 'data', f"{file_name}.xlsx"), 'rb').read()
    return dataset
