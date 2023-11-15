from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def bold_specific_words(value):
    # List of specific words to make bold
    bold_words = ['Meal Plan:', 'Workout Plan:', 'Note:', "Rest Plan:"]

    # Wrap each bold word with <strong> HTML tag
    for word in bold_words:
        value = value.replace(word, f'<strong>{word}</strong>')

    return mark_safe(value)