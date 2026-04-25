
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list of truncated links for embedding
            embeds = []
            for i in classicallist:
                link = i.link
                embed = link[16:]  # Truncate URL
                embeds.append(embed)

            template_values = {
                "logouturl": logout,
                "embeds": embeds  # Pass the list of embeds to the template
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
