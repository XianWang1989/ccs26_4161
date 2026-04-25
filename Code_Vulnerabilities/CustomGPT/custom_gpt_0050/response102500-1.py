
import logging
import google.cloud.logging
from google.cloud.logging import Client as CloudLoggingClient
from google.cloud.logging.handlers import CloudLoggingHandler
import webapp2

# Set up Cloud Logging
client = CloudLoggingClient()
handler = CloudLoggingHandler(client)
logging.getLogger().addHandler(handler)
logging.basicConfig(level=logging.DEBUG)

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
        self.redirect('/welcome')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', Register),
    ('/welcome', Welcome)
], debug=True)
