menu = [
]


class DataMixin:

    def get_user_context(self, **kw):
        context = kw
        context['menu'] = menu
        return context
