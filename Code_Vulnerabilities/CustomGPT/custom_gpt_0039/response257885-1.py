
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to hold the embedded links
            embeds = []
            for suggestion in classicallist:
                link = suggestion.link
                # Extract the video ID
                video_id = link.split('/')[-1].split('?')[0]  # Adjust as needed
                embeds.append(video_id)

            # Prepare values for the template
            template_values = {
                "logouturl": logout,
                "embeds": embeds
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
