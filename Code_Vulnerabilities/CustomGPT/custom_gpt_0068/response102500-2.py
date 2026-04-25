
import logging
import webapp2
import sys

LOG_FILENAME = '/home/me/logs/mylog.txt'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    handlers=[
                        logging.FileHandler(LOG_FILENAME),
                        logging.StreamHandler(sys.stdout),
                    ])

class Handler(webapp2.RequestHandler):
    pass

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
        logging.debug('Main page accessed')
        self.redirect('/welcome')

app = webapp2.WSGIApplication([('/', MainPage), ('/signup', Welcome)], debug=True)
