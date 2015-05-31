from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(str(key))

def get_score_from_concert_answer(dictionary, cindex, aindex):
  pass
