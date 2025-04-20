from django import template
import sys

# Print debugging information
print("Loading custom_filters.py")
print(f"Python path: {sys.path}")

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    """Multiplies the value by the argument"""
    print(f"multiply filter called with {value} and {arg}")
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return '' 