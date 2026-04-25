
import logging
import google.cloud.logging
from google.cloud.logging import DESCENDING
from google.cloud.logging.handlers import CloudLoggingHandler
import webapp2

# Set up Google Cloud logging
client = google.cloud.logging.Client()
handler = CloudLoggingHandler(client)
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[handler]
)

class Handler(webapp2.RequestHandler):
    pass  # Implement your base handler logic if needed

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
