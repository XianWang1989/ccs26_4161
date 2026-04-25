
class Welcome(Handler):
    def get(self):
        if self.user:
            logging.debug('Welcome page accessed for user: %s', self.user.name)
            self.render('welcome.html', username=self.user.name)
        else:
            logging.debug('User not found, redirecting to signup.')
            self.redirect('/signup')
