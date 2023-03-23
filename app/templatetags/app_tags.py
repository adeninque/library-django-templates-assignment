from django import template

from ..models import Book


register: template.Library = template.Library()

@register.inclusion_tag('app/tag/book_card.html')
def book_card(book: Book):
  return {'book': book}

