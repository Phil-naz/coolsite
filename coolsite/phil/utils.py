menu = [{'name': 'Мои HARD & SOFT скилы', 'url_name': 'phil_about'},
        {'name': 'Книги и цитаты', 'url_name': 'books'},
        {'name': 'Заметки', 'url_name': 'texts'},
        {'name': 'Замеры тела', 'url_name': 'measurements_making'},
        ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context