
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical_entries = suggestions.query(suggestions.genre == "classical").order(-suggestions.date).fetch(4)

            # Gather the links for embedding
            embeds = []
            for entry in classical_entries:
                link = entry.link
                embed = link.split('/')[-1]  # Extract video ID from the URL
                embeds.append(embed)

            template_values = {
                "logouturl": logout,
                "links": embeds
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
