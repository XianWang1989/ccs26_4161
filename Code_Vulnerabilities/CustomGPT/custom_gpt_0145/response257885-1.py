
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to hold the truncated video links
            embeds = []
            for i in classicallist:
                link = i.link
                # Truncate the YouTube URL to get the video ID
                embed = link.split('watch?v=')[-1]  # Extract the video ID
                embeds.append(embed)

            # Now embed holds a list of the video IDs
            template_values = {
                "logouturl": logout,
                "embeds": embeds  # Pass the list of video IDs to the template
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
