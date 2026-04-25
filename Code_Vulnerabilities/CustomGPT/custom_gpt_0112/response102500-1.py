
import logging
from google.cloud import logging as gcloud_logging
import webapp2

# Initialize Cloud Logging
client = gcloud_logging.Client()
client.setup_logging()

# Custom RequestHandler
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
