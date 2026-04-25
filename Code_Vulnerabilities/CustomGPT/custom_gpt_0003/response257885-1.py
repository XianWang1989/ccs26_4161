
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to hold the embedded video links
            embeds = []
            for i in classicallist:
                link = i.link
                # Extract the video ID from the URL
                video_id = link.split("v=")[-1]  # Assuming link is in the format: https://www.youtube.com/watch?v=VIDEO_ID
                embeds.append(video_id)

            # Prepare template values including the list of embeds
            template_values = {"logouturl": logout, "embeds": embeds}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
