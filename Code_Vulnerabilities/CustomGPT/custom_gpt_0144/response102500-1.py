import logging
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.debug('This is a debug message')
        logging.info('This is an info message')
        logging.warning('This is a warning message')
        logging.error('This is an error message')
        logging.critical('This is a critical message')
        self.response.out.write('Logging example.')

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
