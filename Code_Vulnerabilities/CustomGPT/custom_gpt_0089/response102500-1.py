
import logging
import webapp2

class Handler(webapp2.RequestHandler):
    pass  # Your existing handler methods

class Welcome(Handler):
    def get(self):
        if self.user:
            logging.debug('Rendering welcome page for user: %s', self.user.name)
            self.render('welcome.html', username=self.user.name)
        else:
            logging.debug('Redirect to signup')
            self.redirect('/signup')

class MainPage(Handler):
    def get(self):
        self.redirect('/welcome')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', Register),
    ('/welcome', Welcome)
], debug=True)

# Here’s a basic setup that includes logs:
def log_setup():
    logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    log_setup()
