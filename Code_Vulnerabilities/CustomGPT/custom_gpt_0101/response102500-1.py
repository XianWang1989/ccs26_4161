
import logging
import webapp2

LOG_FILENAME = '/home/me/logs/mylog.txt'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

class Handler(webapp2.RequestHandler):
    pass  # Your existing Handler code

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
        logging.debug('Redirecting to welcome page')
        self.redirect('/welcome')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', Register),
    ('/welcome', Welcome)
], debug=True)

# Ensure that logging is captured by the app engine's logging service
logging.getLogger().addHandler(logging.StreamHandler())
