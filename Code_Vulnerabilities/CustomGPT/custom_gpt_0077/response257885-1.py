
class ClassicalPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Prepare a list to hold the truncated embed links
            embeds = []
            for suggestion in classicallist:
                link = suggestion.link
                # Extract the video ID (the part after "v=")
                video_id = link.split('v=')[1]
                # Add to embed list
                embeds.append(video_id)

            # Ensure we have exactly 4 embed links
            while len(embeds) < 4:
                embeds.append("")  # Add empty strings if less than 4

            template_values = {
                "logouturl": logout,
                "links": embeds  # Pass the list to the template
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
