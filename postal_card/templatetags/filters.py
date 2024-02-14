# Put you code here
from django import template

register = template.Library()

@register.filter
def english_to_persian(text):
    persian_digits = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹'
    }
    for eng, per in persian_digits.items():
        text = text.replace(eng, per)
    return text
