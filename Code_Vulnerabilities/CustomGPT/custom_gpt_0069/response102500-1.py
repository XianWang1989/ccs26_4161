
import logging
import google.cloud.logging
from google.cloud.logging import Client
from google.cloud.logging.handlers import CloudLoggingHandler
import webapp2

# Initialize the Cloud Logging client
client = google.cloud.logging.Client()
handler = CloudLoggingHandler(client)
logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger().addHandler(handler)

class Handler(webapp2.RequestHandler):
    pass

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
