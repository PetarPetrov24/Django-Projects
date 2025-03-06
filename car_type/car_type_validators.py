from django.core.exceptions import ValidationError


class CarTypeYearValidator:
    def __init__(self, message="Year must be between 1999 and 2030!"):
        self.message = message

    def __call__(self, value: int):
        if not 1999 <= value <= 2030:
            raise ValidationError(self.message)