
class Hi(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
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

Goodbye().bye()
Hi().printer()
