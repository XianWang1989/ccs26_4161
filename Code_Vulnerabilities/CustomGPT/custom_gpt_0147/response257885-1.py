
import webapp2
import datetime
from google.appengine.ext import ndb
from google.appengine.api import users
from jinja2 import Environment, FileSystemLoader

# Define ndb model
class Suggestions(ndb.Model):
    link = ndb.StringProperty(required=True)
    genre = ndb.StringProperty(required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)

# Jinja2 environment setup
JINJA_ENVIRONMENT = Environment(loader=FileSystemLoader('path/to/templates'))

# Handler to store suggestions
class SuggestionNDB(webapp2.RequestHandler):
    def post(self):
        suggestion = Suggestions()
        suggestion.link = self.request.get("suggestlink")
        suggestion.genre = self.request.get("suggestgenre")
        suggestion.put()
        self.redirect("/")

# Handler to display videos
class ClassicalPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = Suggestions.query(Suggestions.genre == "classical").order(-Suggestions.date)
            classicallist = classical.fetch(4)

            # Prepare links for embedding
            embeds = []
            for suggestion in classicallist:
                link = suggestion.link
                video_id = link.split('v=')[1] if 'v=' in link else ''
                embed_link = f"https://www.youtube.com/embed/{video_id}"
                embeds.append(embed_link)

            # Prepare template variables
            template_values = {
                "logouturl": logout,
                "embed_links": embeds
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")

# HTML Template (classical.html)
"""
<div id="genrelist" name="genrelist">
    <h2 id="genretitle">♪ Classical ♪</h2>
    {% for embed_link in embed_links %}
        <iframe width="480" height="360" src="{{ embed_link }}" frameborder="0" allowfullscreen></iframe>
    {% endfor %}
</div>
"""
