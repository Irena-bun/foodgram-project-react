import re
from django.core.exceptions import ValidationError


def validate_username(username):
    bad_symbols = re.sub(r'\w', '', username)
    if bad_symbols:
        raise ValidationError(f'Недопустимые символы: {bad_symbols}')


def validate_email(email):
#    bad_symbols = re.sub(r'^[\w.@+-]+$', '', email)
#    if bad_symbols:
#        raise ValidationError(f'Недопустимые символы: {bad_symbols}')
#    emails = 
    for m in email:
        bad_symbols = re.sub(r'^[\w.@+-]+$', '', m)
        if bad_symbols:
            print(m, f'Недопустимые символы: {bad_symbols}')
