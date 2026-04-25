
class ClassicalPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical_suggestions = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical_suggestions.fetch(4)

            # Collect links for embedding
            embeds = []
            for i in classicallist:
                link = i.link
                video_id = link.split("v=")[-1]  # Extract video ID
                embed_url = f"https://www.youtube.com/embed/{video_id}"
                embeds.append(embed_url)

            template_values = {
                "logouturl": logout,
                "embeds": embeds
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
