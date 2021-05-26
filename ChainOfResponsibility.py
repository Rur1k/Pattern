class HttpHandler:

    def handle(self, code):
        raise NotImplementedError()


class Http404Handler(HttpHandler):

    def handle(self, code):
        if code == 404:
            return 'Страница не найдена'


class Http500Handler(HttpHandler):

    def handle(self, code):
        if code == 500:
            return 'Ошибка сервера'


class Client:
    def __init__(self):
        self._handlers = []

    def add_handler(self, h):
        self._handlers.append(h)

    def response(self, code):
        for h in self._handlers:
            msg = h.handle(code)
            if msg:
                print('Ответ: %s' % msg)
                break
        else:
            print('Код не обработан')


client = Client()
client.add_handler(Http404Handler())
client.add_handler(Http500Handler())
client.response(400)
client.response(404)
client.response(500)