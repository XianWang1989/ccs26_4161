
import logging
import webapp2

# Configure logging to also output to stdout for local development
logging.basicConfig(level=logging.DEBUG)

class Handler(webapp2.RequestHandler):
    pass  # Assume other methods are defined

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
