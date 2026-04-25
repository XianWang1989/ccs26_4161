
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)
            embed_links = []

            for i in classicallist:
                link = i.link
                embed = link.split('/')[-1]  # Extract video ID from the URL
                embed_links.append(embed)  # Store video ID for later use

            template_values = {
                "logouturl": logout,
                "embed_links": embed_links  # Pass the list of links to the template
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
