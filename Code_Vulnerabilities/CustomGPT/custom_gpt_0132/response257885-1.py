
class ClassicalPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical_entries = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical_entries.fetch(4)

            # Extract and format the embeds
            embeds = []
            for entry in classicallist:
                link = entry.link
                embed = link.split('v=')[-1]  # Truncate to get video ID
                embeds.append(embed)

            template_values = {
                "logouturl": logout,
                "embeds": embeds  # Send the list of embeds to the template
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
