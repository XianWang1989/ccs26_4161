
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
                video_id = link.split('/')[-1]  # Adjust to get the video ID correctly
                embed_url = f"https://www.youtube.com/embed/{video_id}"
                embeds.append(embed_url)

            template_values = {"logouturl": logout, "links": embeds}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
