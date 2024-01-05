from django import template

register = template.Library()

bad_words = [
    'Шольц', 'Макрон', 'цунами', 'зверье', 'телеграм',
]


@register.filter()
def censor(value):
    for val in bad_words:
        value = value.replace(val, '***')
    return value
