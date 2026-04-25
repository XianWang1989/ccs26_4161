
import google.cloud.logging
from google.cloud.logging import handlers
import logging
import webapp2

# Set up Google Cloud logging
client = google.cloud.logging.Client()
client.setup_logging()

# Set up a logger
logger = logging.getLogger(__name__)

class Handler(webapp2.RequestHandler):
    ...

class Welcome(Handler):
    def get(self):
        if self.user:
            logger.debug('Rendering welcome page for user: %s', self.user.name)
            self.render('welcome.html', username=self.user.name)
        else:
            logger.debug('Redirecting to signup')
            self.redirect('/signup')

class MainPage(Handler):
    def get(self):
        self.redirect('/welcome')

app = webapp2.WSGIApplication([('/', MainPage), ('/signup', Register), ('/welcome', Welcome)], debug=True)
