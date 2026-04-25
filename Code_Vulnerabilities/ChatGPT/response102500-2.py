
class MainPage(Handler):
    def get(self):
        logging.debug('MainPage accessed')
        self.redirect('/welcome')
