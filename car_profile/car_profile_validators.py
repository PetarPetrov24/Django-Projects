from django.core.exceptions import ValidationError


class CarUsernameValidator:
    def __init__(self, message="Username must be at least 3 chars long!"):
        self.message = message

    def __call__(self, value: str):
        if not isinstance(value, str):
            raise ValidationError("Username must be a string!")

        if len(value) < 3:
            raise ValidationError(self.message)

class CarUsernameContainsValidator:
    def __init__(self, message="Username must contain only letters, digits, and underscores!"):
        self.message = message

    def __call__(self, value):
        if not isinstance(value, str):
            raise ValidationError("Username must be a string!")

        if not value.isidentifier():
            raise ValidationError(self.message)


