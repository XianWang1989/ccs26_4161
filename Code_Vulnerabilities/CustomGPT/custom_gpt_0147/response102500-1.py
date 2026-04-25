
import logging
import webapp2
from google.cloud import logging as cloud_logging

# Initialize Cloud Logging
client = cloud_logging.Client()
client.setup_logging()

class Handler(webapp2.RequestHandler):
    pass

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
        logging.debug('Redirecting to welcome page')
        self.redirect('/welcome')

app = webapp2.WSGIApplication([('/', MainPage), ('/signup', Register), ('/welcome', Welcome)], debug=True)

# Enable debug logging to console as fallback for local development
logging.getLogger().setLevel(logging.DEBUG)
