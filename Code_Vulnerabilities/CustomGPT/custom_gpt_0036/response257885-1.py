
class ClassicalPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Prepare a list to store embedded URLs
            embeds = []
            for i in classicallist:
                link = i.link
                # Truncate the URL to get just the video ID
                video_id = link.split('v=')[1]
                embed_url = f"https://www.youtube.com/embed/{video_id}"
                embeds.append(embed_url)

            # Make sure you have the right number of embeds (4)
            while len(embeds) < 4:
                embeds.append("")  # This ensures all four iframes are rendered

            template_values = {"logouturl": logout, "embeds": embeds}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
