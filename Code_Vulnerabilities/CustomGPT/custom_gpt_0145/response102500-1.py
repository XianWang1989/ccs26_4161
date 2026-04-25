
import logging
import google.cloud.logging
from google.cloud.logging import Client
from google.cloud.logging.handlers import CloudLoggingHandler
import webapp2

# Create a client and set up the logging handler
client = Client()
handler = CloudLoggingHandler(client)
logging.basicConfig(
    handlers=[handler],
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s'
)

class Handler(webapp2.RequestHandler):
    # Your handler code here

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

app = webapp2.WSGIApplication([('/', MainPage),('/signup', Register),('/welcome', Welcome)], debug=True)
