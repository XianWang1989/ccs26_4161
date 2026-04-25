
import logging
import sys
from google.appengine.ext import webapp2

# Set up logging
LOG_FILENAME = '/home/me/logs/mylog.txt'
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILENAME),  # Log to a file
        logging.StreamHandler(sys.stdout)    # Log to console
    ]
)

class Handler(webapp2.RequestHandler):
    pass  # Placeholder for your custom logic if needed

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
