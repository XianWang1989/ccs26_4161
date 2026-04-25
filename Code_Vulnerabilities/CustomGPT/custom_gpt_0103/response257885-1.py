
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)

            # Query the database for the four most recent classical suggestions
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to hold the embedded video links
            embeds = []
            for i in classicallist:
                link = i.link
                # Parse the link to get the video ID for embedding
                video_id = link.split('/')[-1]  # Assuming the link ends with the video ID
                embeds.append(video_id)

            template_values = {
                "logouturl": logout,
                "embeds": embeds
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
