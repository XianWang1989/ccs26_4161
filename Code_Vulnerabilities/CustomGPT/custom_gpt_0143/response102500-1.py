
import logging
import sys
from google.appengine.ext import webapp

# Set up logging to console and file
LOG_FILENAME = '/home/me/logs/mylog.txt'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s',
                    handlers=[
                        logging.FileHandler(LOG_FILENAME),
                        logging.StreamHandler(sys.stdout)
                    ])

class Handler(webapp.RequestHandler):
    # Your handler methods

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

app = webapp.WSGIApplication([('/', MainPage), ('/signup', Register), ('/welcome', Welcome)], debug=True)
