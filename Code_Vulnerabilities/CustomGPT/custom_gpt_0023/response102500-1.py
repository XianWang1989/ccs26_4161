
import logging
import google.cloud.logging
from google.cloud.logging import DESCENDING
from google.cloud.logging.handlers import CloudLoggingHandler
from google.cloud.logging.handlers import setup_logging
import webapp2

# Configure Google Cloud Logging
client = google.cloud.logging.Client()
handler = CloudLoggingHandler(client)
setup_logging(handler)

class Handler(webapp2.RequestHandler):
    pass

class Welcome(Handler):
    def get(self):
        if self.user:
            logging.debug('Rendering welcome page for user')            
            self.render('welcome.html', username=self.user.name)
        else:
            logging.debug('Redirect to signup')            
            self.redirect('/signup')

class MainPage(Handler):
    def get(self):
        self.redirect('/welcome')

app = webapp2.WSGIApplication([('/', MainPage), ('/signup', Register), ('/welcome', Welcome)], debug=True)
