import re
from django.core.exceptions import ValidationError


def validate_username(username):
    bad_symbols = re.sub(r'\w', '', username)
    if bad_symbols:
        raise ValidationError(f'Недопустимые символы '
                              f'в имени: {bad_symbols}'
                              )

# def validate_email(email):
#    validate = re.sub(r'^[\w.@+-]+$', '', email)
#    if validate:
#        bad_symbols = re.sub(
#            r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', '', email)
#        raise ValidationError(f'Недопустимые символы '
#                              f'в email: {bad_symbols}'


def get_bad_symbols(email: str) -> str:
    return re.sub(r'\w|@|\.', '', email)


def check_email_form(email) -> bool:
    return re.fullmatch(r'\w+@\w+\.\w+', email)


def validate_email(email):
    bad_symbols = get_bad_symbols(email)
    if bad_symbols:
        raise ValidationError(f'Недопустимые символы в email: {bad_symbols}')
    if not check_email_form(email):
        raise ValidationError('Недопустимый формат email')
