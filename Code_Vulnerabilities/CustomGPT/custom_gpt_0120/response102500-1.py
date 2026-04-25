
import logging
import os
from google.appengine.ext.webapp import WSGIApplication, RequestHandler

LOG_FILENAME = os.path.join(os.path.expanduser('~'), 'logs', 'mylog.txt')
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler(LOG_FILENAME)])

class Handler(RequestHandler):
    pass

class Welcome(Handler):
    def get(self):
        if self.user:
            logging.debug('Rendering welcome page for user %s', self.user.name)            
            self.render('welcome.html', username=self.user.name)
        else:
            logging.debug('Redirect to signup')            
            self.redirect('/signup')

class MainPage(Handler):
    def get(self):
        self.redirect('/welcome')

app = WSGIApplication([('/', MainPage),('/signup', Register),('/welcome', Welcome)], debug=True)

if __name__ == '__main__':
    logging.info('Starting app...')
