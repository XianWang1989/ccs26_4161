
import logging
import sys
from google.cloud import logging as gcloud_logging
from google.cloud.logging import DESCENDING

# Setup Google Cloud Logging
client = gcloud_logging.Client()
client.setup_logging()

# Optionally, log to a file as well
LOG_FILENAME = '/home/me/logs/mylog.txt'
file_handler = logging.FileHandler(LOG_FILENAME)
file_handler.setLevel(logging.DEBUG)
logging.getLogger().addHandler(file_handler)

# Log messages to stdout as well
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
logging.getLogger().addHandler(stdout_handler)

# Set the logging level
logging.basicConfig(level=logging.DEBUG)

class Handler(webapp2.RequestHandler):
    ...

class Welcome(Handler):
    def get(self):
        if self.user:
            logging.debug('rendering welcome page for user: %s', self.user.name)            
            self.render('welcome.html', username=self.user.name)
        else:
            logging.debug('redirect to signup')            
            self.redirect('/signup')

class MainPage(Handler):
    def get(self):
        self.redirect('/welcome')

app = webapp2.WSGIApplication([('/', MainPage),('/signup', Register),('/welcome', Welcome)], debug=True)
