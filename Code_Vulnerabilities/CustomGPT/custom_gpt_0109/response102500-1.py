
import logging
import google.cloud.logging
from google.cloud.logging import DESCENDING
from google.cloud.logging.handlers import CloudLoggingHandler

# Initialize Google Cloud Logging
client = google.cloud.logging.Client()
handler = CloudLoggingHandler(client)

# Use default logging configuration
logging.basicConfig(
    handlers=[handler],
    level=logging.DEBUG
)

class Handler(webapp2.RequestHandler):
    pass  # Your existing implementation

class Welcome(Handler):
    def get(self):
        if self.user:
            logging.debug('Rendering welcome page for user')            
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
