
import logging
import webapp2

# Configure logging to use the console
logging.basicConfig(level=logging.DEBUG)  # Logs will be printed to the console

class Handler(webapp2.RequestHandler):
    pass  # Your base handler logic

class Welcome(Handler):
    def get(self):
        if self.user:
            logging.debug('Rendering welcome page for user: %s', self.user.name)            
            self.render('welcome.html', username=self.user.name)
        else:
            logging.debug('Redirecting to signup')            
            self.redirect('/signup')

class MainPage(Handler):
    def get(self):
        self.redirect('/welcome')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', Register),
    ('/welcome', Welcome)
], debug=True)
