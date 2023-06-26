import re
from django.core.exceptions import ValidationError


def validate_username(username):
    bad_symbols = re.sub(r'\w', '', username)
    if bad_symbols:
        raise ValidationError(f'Недопустимые символы '
                              f'в имени: {bad_symbols}'
                              )


def validate_email(email):
    bad_symbols = re.sub(r'^[\w.@+-]+$', '', email)
    if bad_symbols:
        bad_symbols2 = re.sub(r'/\A[^@]+@([^@\.]+\.)+[^@\.]+\z/', '', email)
        raise ValidationError(f'Недопустимые символы '
                              f'в email: {bad_symbols2}'
                              )
