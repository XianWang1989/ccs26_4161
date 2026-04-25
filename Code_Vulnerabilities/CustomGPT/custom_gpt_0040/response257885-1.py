
class ClassicalPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to hold the embedded links
            embeds = []
            for i in classicallist:
                link = i.link
                # Extract the video ID from the URL
                video_id = link.split("v=")[-1]  # Extract video ID
                ampersand_position = video_id.find("&")
                if ampersand_position != -1:
                    video_id = video_id[:ampersand_position]  # Trim any query parameters
                embeds.append(video_id)  # Add to the list

            template_values = {"logouturl": logout, "embeds": embeds}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
