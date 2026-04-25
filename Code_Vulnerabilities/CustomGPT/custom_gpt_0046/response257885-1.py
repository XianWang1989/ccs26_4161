
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to store the embed links
            embeds = []
            for i in classicallist:
                link = i.link
                # Extract the video ID from the YouTube share link
                embed = link.split('v=')[1] if 'v=' in link else link
                # Handle the case where there might be additional parameters in the URL
                embed = embed.split('&')[0]
                embeds.append(embed)

            # Pass the list of embeds to the template
            template_values = {"logouturl": logout, "embeds": embeds}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
