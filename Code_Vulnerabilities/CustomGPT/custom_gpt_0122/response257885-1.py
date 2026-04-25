
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to hold the embed codes
            embeds = []

            for i in classicallist:
                link = i.link
                # Extract the video ID from the YouTube URL
                embed_id = link.split("v=")[-1]  # In case of full URL
                if "&" in embed_id:
                    embed_id = embed_id.split("&")[0]  # Remove any additional parameters
                embeds.append(embed_id)

            # Prepare template values
            template_values = {"logouturl": logout, "embeds": embeds}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
