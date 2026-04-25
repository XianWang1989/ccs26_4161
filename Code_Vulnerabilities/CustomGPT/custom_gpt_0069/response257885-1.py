
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Prepare a list for the embedded links
            embeds = []
            for i in classicallist:
                link = i.link
                # Truncate the URL to get the video ID
                embed = link.split("v=")[1]
                if "&" in embed:
                    embed = embed.split("&")[0]  # Make sure to truncate at any additional parameters
                embeds.append(embed)

            template_values = {"logouturl": logout, "embeds": embeds}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
