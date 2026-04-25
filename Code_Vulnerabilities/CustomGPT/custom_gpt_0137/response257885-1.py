
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to hold the embedded IDs
            embedded_links = []

            for i in classicallist:
                link = i.link
                # Truncate the URL to get the video ID
                embed = link.split('v=')[1] if 'v=' in link else link[16:]  # Can also handle other types of YouTube URLs
                embedded_links.append(embed)

            # Prepare template values with the list of embedded links
            template_values = {"logouturl": logout, "links": embedded_links}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
