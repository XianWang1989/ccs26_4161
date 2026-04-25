
import logging
import webapp2
from google.cloud import logging as cloud_logging

# Initialize Google Cloud logging
client = cloud_logging.Client()
client.setup_logging()

class Handler(webapp2.RequestHandler):
    pass  # Implement common functionality if needed

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
    ('/signup', Register),  # Make sure Register is defined
    ('/welcome', Welcome)
], debug=True)
