
class Welcome(Handler):
    def get(self):
        user_name = self.user.name if self.user else 'guest'
        logging.debug('Rendering welcome page for user: %s', user_name)
        self.render('welcome.html', username=user_name)
