from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def bold_specific_words(value):
    bold_words = ['Meal Plan:', 'Workout Plan:', 'Note:', "Rest Plan:" ,"Plan:"]
    for word in bold_words:
        value = value.replace(word, f'<strong>{word}</strong>')
    return mark_safe(value)