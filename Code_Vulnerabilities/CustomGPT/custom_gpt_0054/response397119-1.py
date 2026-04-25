
class Hi(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Hi, cls).__new__(cls)
            cls._instance.answer = 'hi'
        return cls._instance

    def change(self):
        self.answer = 'bye'
        print(self.answer)

    def printer(self):
        print(self.answer)


class Goodbye(object):
    def bye(self):
        Hi().change()


goodbye = Goodbye()
goodbye.bye()
hi_instance = Hi()
hi_instance.printer()
