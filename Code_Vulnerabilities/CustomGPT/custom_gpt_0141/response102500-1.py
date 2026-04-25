
import logging
import webapp2

# Configure logging to App Engine's standard logging
logging.basicConfig(level=logging.DEBUG)

# Default logging handler that will route logs to Google Cloud Logging
logger = logging.getLogger()

class Handler(webapp2.RequestHandler):
    # Abstract base handler class
    pass

class Welcome(Handler):
    def get(self):
        if self.user:
            logger.debug('Rendering welcome page for user: %s', self.user.name)
            self.render('welcome.html', username=self.user.name)
        else:
            logger.debug('Redirect to signup')
            self.redirect('/signup')

class MainPage(Handler):
    def get(self):
        self.redirect('/welcome')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', Register),
    ('/welcome', Welcome)
], debug=True)
