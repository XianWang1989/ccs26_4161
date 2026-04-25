
class Hi(object):
    answer = 'hi'  # Class variable

    def change(self):
        Hi.answer = 'bye'
        print(Hi.answer)

    def printer(self):
        print(Hi.answer)

class Goodbye(object):
    def bye(self):
        hi_instance = Hi()
        hi_instance.change()

# Create instances and call methods
goodbye = Goodbye()
goodbye.bye()
hi_instance = Hi()
hi_instance.printer()
