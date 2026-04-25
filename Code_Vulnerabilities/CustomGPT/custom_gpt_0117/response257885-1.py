
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Extracting the embed links
            embeds = []
            for i in classicallist:
                link = i.link
                # Truncate the URL to get the video ID
                video_id = link.split('/')[-1].split('?v=')[-1]  # Updated for different link formats
                embeds.append(video_id)

            template_values = {"logouturl": logout, "embeds": embeds}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
