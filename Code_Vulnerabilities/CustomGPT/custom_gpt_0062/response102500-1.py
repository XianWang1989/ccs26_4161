
import logging
from google.cloud import logging as cloud_logging
from google.cloud.logging import DESCENDING
import webapp2

# Initialize Cloud Logging
client = cloud_logging.Client()
client.setup_logging()

# Optional: Define a logger
logger = logging.getLogger(__name__)

class Handler(webapp2.RequestHandler):
    pass  # Your existing handler methods

class Welcome(Handler):
    def get(self):
        if self.user:
            logger.debug('Rendering welcome page for user: %s', self.user.name)            
            self.render('welcome.html', username=self.user.name)
        else:
            logger.debug('Redirect to signup')            
            self.redirect('/signup')

class MainPage(Handler):
    def get(self):
        self.redirect('/welcome')

app = webapp2.WSGIApplication([('/', MainPage), ('/signup', Register), ('/welcome', Welcome)], debug=True)
