
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list for the video IDs
            video_ids = []
            for i in classicallist:
                link = i.link
                embed = link.split("v=")[1]  # Extract video ID from the URL
                video_ids.append(embed)

            template_values = {
                "logouturl": logout,
                "video_ids": video_ids  # Pass the list of video IDs to the template
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
