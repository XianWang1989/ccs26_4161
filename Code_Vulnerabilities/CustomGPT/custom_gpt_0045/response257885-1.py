
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)
            # Create a list to hold the embed links
            embeds = []
            for i in classicallist:
                link = i.link
                embed = link.split("v=")[-1]  # Get the video ID from the link
                embed_url = f"https://www.youtube.com/embed/{embed}"  # Create the embed URL
                embeds.append(embed_url)

            template_values = {"logouturl": logout, "embeds": embeds}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
