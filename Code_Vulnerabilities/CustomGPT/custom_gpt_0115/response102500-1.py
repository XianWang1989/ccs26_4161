
import logging
import google.cloud.logging
from google.cloud.logging import DESCENDING
from google.cloud import logging as cloud_logging

# Initialize Cloud Logging
client = cloud_logging.Client()
client.setup_logging()

# Configure the logging level
logging.basicConfig(level=logging.DEBUG)

class Handler(webapp2.RequestHandler):
    # Your existing code...

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
