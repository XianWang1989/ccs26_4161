
class ClassicalPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical_suggestions = suggestions.query(suggestions.genre == "classical").order(-suggestions.date).fetch(4)
            embeds = []

            for suggestion in classical_suggestions:
                link = suggestion.link
                embed = link.split('v=')[1] if 'v=' in link else link[16:]  # Extracting the video ID
                embeds.append(embed)

            template_values = {
                "logouturl": logout,
                "embeds": embeds
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
