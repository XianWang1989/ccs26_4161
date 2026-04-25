
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            embeds = []
            for i in classicallist:
                link = i.link
                # Extract the video ID from the URL
                embed = link.split("v=")[-1].split("&")[0]
                embeds.append(embed)  # Append each embed ID to the list

            template_values = {
                "logouturl": logout,
                "video_embeds": embeds  # Pass the list of embeds to the template
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
