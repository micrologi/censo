from django.core.exceptions import ValidationError

def validate_inrange(value, rangeini, rangefin):
    if (value < rangeini) or (value > rangefin):
        raise ValidationError(
            _("%(value)s deve estar "),
            params={"value": value},
        )
