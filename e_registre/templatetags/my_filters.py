from django import template

register = template.Library()
print("test filtre") 

@register.filter
def item(value, arg):
	return value[arg]