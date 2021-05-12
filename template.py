class Template:
    def template_method(self):
        self.one()
        self.two()
        self.three()

    def one(self):
        print('Базовый вызов первой функции')

    def two(self):
        print('Базовый вызов второй функции')

    def three(self):
        print('Базовый вызов третей функции')

class TemlateNew(Template):
    def one(self):
        print('Применен шаблонный метод для вызова первой функции')

    def two(self):
        print('Применен шаблонный метод для вызова второй функции')

    def three(self):
        print('Применен шаблонный метод для вызова третей функции')

template = TemlateNew()

template.template_method()

