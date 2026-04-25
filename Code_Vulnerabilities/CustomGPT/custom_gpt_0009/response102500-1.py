
import logging
from google.cloud import logging as cloud_logging

# Instantiate a Google Cloud Logging client
client = cloud_logging.Client()
client.setup_logging()

# Set the logging level
logging.basicConfig(level=logging.DEBUG)

class Handler(webapp2.RequestHandler):
    pass

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

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', Register),
    ('/welcome', Welcome)
], debug=True)
