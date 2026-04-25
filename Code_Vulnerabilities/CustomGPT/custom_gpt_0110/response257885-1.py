
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to store the embedded links
            embed_links = []
            for suggestion in classicallist:
                link = suggestion.link
                embed = link.split("/")[-1]  # Extract video ID from the URL
                embed_links.append(embed)

            # Pass the list of embed links to the template
            template_values = {
                "logouturl": logout,
                "embed_links": embed_links
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
