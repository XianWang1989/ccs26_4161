
import logging
import google.cloud.logging
from google.cloud.logging import DESCENDING
import webapp2

# Initialize the Google Cloud Logging client
client = google.cloud.logging.Client()
client.setup_logging()

# Logging configuration
LOG_FILENAME = '/home/me/logs/mylog.txt'  # Local file logging (optional)
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

class Handler(webapp2.RequestHandler):
    ...

class Welcome(Handler):
    def get(self):
        if self.user:
            logging.debug('rendering welcome page for user')
            self.render('welcome.html', username=self.user.name)
        else:
            logging.debug('redirect to signup')
            self.redirect('/signup')

class MainPage(Handler):
    def get(self):
        self.redirect('/welcome')

app = webapp2.WSGIApplication([('/', MainPage), ('/signup', Register), ('/welcome', Welcome)], debug=True)
