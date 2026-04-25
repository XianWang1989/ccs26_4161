
import logging
import webapp2

# Configure global logging settings
LOG_FILENAME = '/home/me/logs/mylog.txt'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(message)s')

# Add a console handler to log to stdout as well
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logging.getLogger().addHandler(console_handler)

class Handler(webapp2.RequestHandler):
    pass

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

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', Register),
    ('/welcome', Welcome)
], debug=True)
