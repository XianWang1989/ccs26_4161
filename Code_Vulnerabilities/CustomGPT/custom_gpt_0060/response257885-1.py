
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Prepare a list to hold the embedded links
            embed_links = []
            for i in classicallist:
                link = i.link
                # Truncate the link to get the video ID
                embed_id = link.split('v=')[1].split('&')[0]  # Get video ID
                embed_links.append(embed_id)  # Append the video ID to the list

            # Prepare the template data
            template_values = {"logouturl": logout, "embed_links": embed_links}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
