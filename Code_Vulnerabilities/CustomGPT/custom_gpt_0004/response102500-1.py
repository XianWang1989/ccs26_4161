
import logging
import google.cloud.logging
from google.cloud.logging import DESCENDING
from google.cloud.logging.handlers import AppEngineHandler
import webapp2

# Initialize Google Cloud Logging
client = google.cloud.logging.Client()
client.setup_logging()

# This handler logs to the Cloud Logging
logging.getLogger().setLevel(logging.DEBUG)
handler = AppEngineHandler()
logging.getLogger().addHandler(handler)

class Handler(webapp2.RequestHandler):
    pass

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

