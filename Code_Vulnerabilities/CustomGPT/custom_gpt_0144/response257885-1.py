class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)
            embed_links = []

            for i in classicallist:
                # Extract the video ID from the YouTube URL
                video_id = i.link.split("youtu.be/")[-1] if "youtu.be/" in i.link else i.link.split("v=")[-1]
                embed_links.append(video_id)

            template_values = {
                "logouturl": logout,
                "links": embed_links  # list of video IDs
            }

            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
