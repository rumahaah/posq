from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
register = template.Library()

@register.simple_tag
def multiply(qty, price, *args, **kwargs):
	if price:
		subtotal = price * qty
	return intcomma(int(subtotal))