import gdata.auth
import gdata.calendar.service
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import os
import urllib

# Add your own OAuth consumer key and secret
CONSUMER_KEY = 'my-app.appspot.com'
CONSUMER_SECRET = 'consumersecret'

# Set up your OAuth client
def getClient():
    client = gdata.calendar.service.CalendarService()
    client.SetOAuthInputParameters(
        gdata.auth.OAuthSignatureMethod.HMAC_SHA1,
        consumer_key=CONSUMER_KEY, 
        consumer_secret=CONSUMER_SECRET)
    return client

# OpenID Handler
class OpenIDHandler(webapp.RequestHandler):
    def get(self):
        """Begins the OpenID flow and adds OAuth to authentication request."""
        login_url = users.create_login_url(dest_url='http://my-app.appspot.com/oauth')
        self.redirect(login_url)

# OAuth Flow - Step 1: Request Token
class OAuthOne(webapp.RequestHandler):
    def get(self):
        client = getClient()
        request_token = client.FetchOAuthRequestToken(oauth_callback='http://my-app.appspot.com/oauth2')
        client.SetOAuthToken(request_token)
        auth_url = client.GenerateOAuthAuthorizationURL()
        self.redirect(auth_url)

# OAuth Flow - Step 2: Access Token
class OAuthTwo(webapp.RequestHandler):
    def get(self):
        client = getClient()
        token_from_url = gdata.auth.OAuthTokenFromUrl(self.request.uri)
        if not token_from_url:
            self.redirect('/oauth')
        else:
            client.SetOAuthToken(token_from_url)
            oauth_verifier = self.request.get('oauth_verifier', default_value='')
            client.UpgradeToOAuthAccessToken(oauth_verifier=oauth_verifier)
            self.redirect('/')

# Main page to display user information or deny access
class MainPage(webapp.RequestHandler):
    def get(self):
        self.user = users.get_current_user()
        self.template_values = {}
        if self.user:
            # Here, you can access Google Calendar API or other services using OAuth.
            self.template_file = 'templates/index.html'
        else:
            self.template_file = 'templates/denied.html'

        path = os.path.join(os.path.dirname(__file__), self.template_file)
        self.response.out.write(template.render(path, self.template_values))

# Application URL mapping
application = webapp.WSGIApplication(
    [('/oauth', OAuthOne),
     ('/oauth2', OAuthTwo),
     ('/_ah/login_required', OpenIDHandler),
     ('/', MainPage)],
    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
