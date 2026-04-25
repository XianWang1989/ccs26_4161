
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to hold the embedded YouTube links for each recent entry
            embeds = []
            for i in classicallist:
                link = i.link
                embed = link.split('/')[-1]  # Extract the video ID from the URL
                embeds.append(embed)  # Append the video ID to the list

            # Prepare the template values with a list of embeds
            template_values = {"logouturl": logout, "embeds": embeds}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
