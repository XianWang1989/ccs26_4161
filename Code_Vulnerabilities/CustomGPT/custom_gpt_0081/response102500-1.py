
import logging
import google.cloud.logging
from google.cloud.logging import DESCENDING
from google.cloud.logging import Client

# Initialize the client
client = google.cloud.logging.Client()
client.setup_logging()

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

app = webapp2.WSGIApplication([('/', MainPage), ('/signup', Register), ('/welcome', Welcome)], debug=True)

# Example function to fetch logs
def get_logs():
    client = Client()
    logger = client.logger("my-log")
    entries = logger.list_entries(order_by=DESCENDING)

    for entry in entries:
        print(entry.payload)
