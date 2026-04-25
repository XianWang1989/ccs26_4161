
class ClassicalPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Collect all video IDs for embedding
            embeds = []
            for i in classicallist:
                link = i.link
                # Extract the video ID from the YouTube URL
                embed = link.split("watch?v=")[-1]  # Get the video ID part
                embeds.append(embed)

            template_values = {
                "logouturl": logout,
                "embeds": embeds
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
