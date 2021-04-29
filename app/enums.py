from django.utils.translation import ugettext as _


class RiskCalculationStatus:
    MATCH = 'Match'
    ERROR = 'Error'
    EXCEPTION = 'Exception'

    ENUM = (
        (MATCH, _(MATCH)),
        (ERROR, _(ERROR)),
        (EXCEPTION, _(EXCEPTION))

    )
