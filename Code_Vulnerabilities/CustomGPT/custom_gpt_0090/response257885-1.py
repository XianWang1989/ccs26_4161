
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Collect the embedded links
            embed_links = []
            for i in classicallist:
                link = i.link
                embed = link.split('v=')[1]  # Truncate the URL to get the video ID
                embed_links.append(embed)

            # Prepare template values with the list of embedded links
            template_values = {
                "logouturl": logout,
                "embed_links": embed_links
            }

            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
