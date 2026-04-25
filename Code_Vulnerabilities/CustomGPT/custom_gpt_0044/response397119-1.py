
class Hi(object):
    # Class variable
    answer = 'hi'

    def change(self):
        Hi.answer = 'bye'
        print(Hi.answer)

    def printer(self):
        print(Hi.answer)

class Goodbye(object):
    def bye(self):
        Hi().change()

goodbye = Goodbye()
goodbye.bye()  # Output: 'bye'

hi_instance = Hi()
hi_instance.printer()  # Output: 'bye'
