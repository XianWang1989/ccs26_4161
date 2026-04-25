
import logging
import os
import webapp2

LOG_FILENAME = '/home/me/logs/mylog.txt'

# Ensure the logs folder exists
if not os.path.exists(os.path.dirname(LOG_FILENAME)):
    os.makedirs(os.path.dirname(LOG_FILENAME))

logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

class Handler(webapp2.RequestHandler):
    ...

class Welcome(Handler):
    def get(self):
        if self.user:
            logging.debug('Rendering welcome page for user: %s', self.user.name)            
            self.render('welcome.html', username=self.user.name)
        else:
            logging.debug('Redirecting to signup')            
            self.redirect('/signup')

class MainPage(Handler):
    def get(self):
        self.redirect('/welcome')

app = webapp2.WSGIApplication([('/', MainPage), ('/signup', Register), ('/welcome', Welcome)], debug=True)
