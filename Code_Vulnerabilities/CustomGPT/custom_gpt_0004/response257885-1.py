
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)
            embeds = []

            for i in classicallist:
                link = i.link
                embed = link.split('/')[-1]  # Get the video ID from the URL
                embeds.append(embed)

            template_values = {
                "logouturl": logout,
                "links": embeds  # Pass the list of video IDs
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
