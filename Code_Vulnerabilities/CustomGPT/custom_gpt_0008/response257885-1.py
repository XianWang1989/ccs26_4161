
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # List to hold all the embedded links
            embedded_links = []
            for i in classicallist:
                link = i.link
                embed = link.split("=")[-1]  # Extract video ID from link
                embedded_links.append(embed)

            # Pass the list of embedded links to the template
            template_values = {"logouturl": logout, "embedded_links": embedded_links}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
