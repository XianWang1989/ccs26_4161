
import logging
import os
import webapp2

# Create logs directory if it doesn't exist
LOG_DIR = '/home/me/logs'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILENAME = os.path.join(LOG_DIR, 'mylog.txt')

# Set up logging
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s')

class Handler(webapp2.RequestHandler):
    pass

class Welcome(Handler):
    def get(self):
        if self.user:
            logging.debug('Rendering welcome page for user %s', self.user.name)            
            self.render('welcome.html', username=self.user.name)
        else:
            logging.debug('Redirecting to signup')            
            self.redirect('/signup')

class MainPage(Handler):
    def get(self):
        self.redirect('/welcome')

app = webapp2.WSGIApplication([('/', MainPage), ('/signup', Register), ('/welcome', Welcome)], debug=True)
