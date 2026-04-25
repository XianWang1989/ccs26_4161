
import logging
import webapp2

# Configure the logging to use the Cloud Logging
logging.basicConfig(level=logging.DEBUG)

class Handler(webapp2.RequestHandler):
    pass

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

app = webapp2.WSGIApplication(
    [('/', MainPage), ('/signup', Register), ('/welcome', Welcome)],
    debug=True
)

# Use Cloud Logging to view logs
def main():
    logging.info('App Started')

if __name__ == '__main__':
    main()
