
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
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            embeds = []
            for i in classicallist:
                link = i.link
                embed = link.split('=')[-1]  # Extract video ID from URL
                embeds.append(embed)

            template_values = {"logouturl": logout, "embeds": embeds}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
