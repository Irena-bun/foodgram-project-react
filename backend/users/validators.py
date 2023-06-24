import re
from django.core.exceptions import ValidationError


# def validate_username(value):
#    value_tmp = value.lower()
#    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#           'n', 'o', 'p', 'r', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_']
#
#    for i in range(len(value)):
#        if value_tmp[i] not in abc:
#            raise ValidationError(u'Недопустимые символы ( {} )'.format(
#                value_tmp[i]))
#
#
# def validate_email(value):
#    if not bool(re.match(r'^[\w.@+-]+$', value)):
#        raise ValidationError(
#            'Некорректный email'
#        )
#    return value

def validate_username(username):
    bad_symbols = re.sub(r'\w', '', username)
    if bad_symbols:
        raise ValidationError(f'Некорректное имя.'
                              f'Недопустимые символы: {bad_symbols}')


def validate_email(email):
    bad_symbols = re.sub(r'^[\w.@+-]+$', r'', email)
    if bad_symbols:
        raise ValidationError(f'Некорректный email.'
                              f'Недопустимые символы: {bad_symbols}')
