
import logging
import webapp2

# Configure logging: This will output logs to stderr
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Handler(webapp2.RequestHandler):
    pass  # Your base handler code here

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

app = webapp2.WSGIApplication([('/', MainPage), ('/signup', Register), ('/welcome', Welcome)], debug=True)
