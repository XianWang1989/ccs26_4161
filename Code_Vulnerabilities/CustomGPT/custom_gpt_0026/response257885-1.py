
class ClassicalPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to hold the embed links
            embed_links = []
            for i in classicallist:
                link = i.link
                # Truncate the YouTube share URL to get the video ID
                video_id = link.split("v=")[-1]
                embed_links.append(video_id)

            # Pass the list of embed links to the template
            template_values = {
                "logouturl": logout,
                "embed_links": embed_links
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
