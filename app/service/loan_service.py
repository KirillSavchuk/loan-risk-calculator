from app.models import Loan
from app.enums import RiskCalculationStatus


def calculate_risk_score(loan: Loan) -> int:
    return loan.age * loan.dependents


def calculate_risk_calculation_status(loan: Loan) -> RiskCalculationStatus:
    return RiskCalculationStatus.MATCH
