
import webapp2
import datetime
from google.appengine.ext import ndb
from google.appengine.api import users
from jinja2 import Template  # Add this import for Jinja2 template

# Assuming suggestions is your NDB model
class suggestions(ndb.Model):
    link = ndb.StringProperty()
    genre = ndb.StringProperty()
    date = ndb.DateTimeProperty()

class suggestionndb(webapp2.RequestHandler):
    def post(self):
        suggestion = suggestions()
        suggestion.link = self.request.get("suggestlink")
        suggestion.genre = self.request.get("suggestgenre")
        suggestion.date = datetime.datetime.now()
        suggestion.put()

class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)

            # Fetch the last 4 suggestions for the "classical" genre
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list of embedded URLs
            embeds = []
            for i in classicallist:
                # Truncate the URL to get the video ID
                link = i.link
                embed_id = link.split('/')[-1]  # Assuming the link format is... www.youtube.com/watch?v=videoID
                embeds.append(embed_id)

            # Prepare template values
            template_values = {
                "logouturl": logout,
                "embeds": embeds
            }

            # Load and render the template
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")

app = webapp2.WSGIApplication([
    ('/suggest', suggestionndb),
    ('/classical', classicalpage),
], debug=True)
