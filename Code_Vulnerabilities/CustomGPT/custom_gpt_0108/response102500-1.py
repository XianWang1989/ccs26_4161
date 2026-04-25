
import logging
import googlecloud.logging
from googlecloud.logging import DESCENDING
import webapp2

# Initialize the Google Cloud Logging client
client = googlecloud.logging.Client()
client.setup_logging()

class Handler(webapp2.RequestHandler):
    pass  # Your existing code

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
