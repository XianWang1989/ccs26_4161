
import logging
import webapp2
from google.cloud import logging as cloud_logging

# Initialize client for cloud logging
client = cloud_logging.Client()
client.setup_logging()

# Set up a logger
logger = logging.getLogger(__name__)

class Handler(webapp2.RequestHandler):
    pass

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
        logger.debug('Redirecting to welcome page')
        self.redirect('/welcome')

app = webapp2.WSGIApplication([('/', MainPage), ('/signup', Register), ('/welcome', Welcome)], debug=True)
