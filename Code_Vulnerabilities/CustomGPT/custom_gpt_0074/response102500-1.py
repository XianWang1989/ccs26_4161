
import logging
import google.cloud.logging
from google.cloud.logging import DESCENDING
from google.cloud.logging.handlers import CloudLoggingHandler

# Create a Cloud Logging client
client = google.cloud.logging.Client()
handler = CloudLoggingHandler(client)

# Add the handler to the root logger
logging.basicConfig(level=logging.DEBUG, handlers=[handler])

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
