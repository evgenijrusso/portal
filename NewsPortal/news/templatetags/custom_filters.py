from django import template

register = template.Library()

bad_words = [
    'Шольц', 'Макрон', 'цунами', 'зверье', 'телеграм',
]


@register.filter()
def censor(value):
    for name in bad_words:
        value = value.replace(name, '***')
    return value
