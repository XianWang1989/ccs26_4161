
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # List to hold the embedded links
            embeds = []
            for i in classicallist:
                link = i.link
                # Extract the video ID from the URL
                video_id = link.split("v=")[1].split("&")[0]  # Get the video ID
                embeds.append(video_id)

            template_values = {"logouturl": logout, "links": embeds}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
