menu = [
  {'name': 'home', 'url': 'home'}
]

class DataMixin:
  def get_extra_context(self, **kwargs):
    context = kwargs
    
    context.update({
      'menu': menu
    })
    return context