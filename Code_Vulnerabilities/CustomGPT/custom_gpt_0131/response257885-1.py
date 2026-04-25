
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to hold the modified embed links
            embeds = []
            for i in classicallist:
                link = i.link
                # Truncate the URL and prepare the embed link
                embed = link[link.rfind('/') + 1:]  # Getting the video ID
                embeds.append(embed)

            # Prepare template values with the list of embeds
            template_values = {
                "logouturl": logout,
                "embeds": embeds
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
