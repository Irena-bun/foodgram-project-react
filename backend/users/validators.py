import re
from django.core.exceptions import ValidationError


def validate_username(username):
    bad_symbols = re.sub(r'\w', '', username)
    if bad_symbols:
        raise ValidationError(f'Недопустимые символы '
                              f'в имени: {bad_symbols}'
                              )


def validate_email(email):
    validate = re.sub(r'^[\w.@+-]+$', '', email)
    if validate:
        bad_symbols = re.sub(
            r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9_.+-]', '', email)
        raise ValidationError(f'Недопустимые символы '
                              f'в email: {bad_symbols}'
                              )
