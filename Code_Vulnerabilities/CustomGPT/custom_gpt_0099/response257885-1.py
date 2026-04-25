
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            # Query for the four most recent suggestions for the classical genre
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Prepare a list to hold the embedded links
            embeds = []

            for i in classicallist:
                link = i.link
                # Truncate the URL to get the video ID
                embed = link.split('/')[-1].split('?')[0]  # Handles standard and short URLs
                embeds.append(embed)

            # Pass the list of embeds to the template
            template_values = {"logouturl": logout, "embeds": embeds}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
