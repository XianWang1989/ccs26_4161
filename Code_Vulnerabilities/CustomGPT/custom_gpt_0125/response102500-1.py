
import logging
import google.cloud.logging
from google.cloud.logging import DESCENDING
from google.cloud import logging as cloud_logging
import webapp2

# Initialize the Google Cloud Logging client
client = cloud_logging.Client()
client.setup_logging()

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

app = webapp2.WSGIApplication([('/', MainPage),('/signup', Register),('/welcome', Welcome)], debug=True)

# Example of querying logs
def query_logs():
    logger = client.logger('my-log')
    entries = client.list_entries(order_by=DESCENDING)
    for entry in entries:
        print(entry)
