
import webapp2
import datetime
from google.appengine.ext import ndb
from google.appengine.api import users

class Suggestion(ndb.Model):
    link = ndb.StringProperty()
    genre = ndb.StringProperty()
    date = ndb.DateTimeProperty()

class SuggestionHandler(webapp2.RequestHandler):
    def post(self):
        suggestion = Suggestion()
        suggestion.link = self.request.get("suggestlink")
        suggestion.genre = self.request.get("suggestgenre")
        suggestion.date = datetime.datetime.now()
        suggestion.put()

class ClassicalPageHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical_entries = Suggestion.query(Suggestion.genre == "classical").order(-Suggestion.date).fetch(4)

            # Prepare the list of links to send to the template
            links = [entry.link[32:] for entry in classical_entries if entry.link.startswith("https://youtu.be/")]

            template_values = {"logouturl": logout, "links": links}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")

app = webapp2.WSGIApplication([
    ('/suggest', SuggestionHandler),
    ('/classical', ClassicalPageHandler),
], debug=True)
