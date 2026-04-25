
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Prepare a list of video embed links
            embeds = []
            for i in classicallist:
                link = i.link
                embed_url = link.split("v=")[-1]  # Extract video ID from the URL
                embed = f"https://www.youtube.com/embed/{embed_url}"
                embeds.append(embed)

            # Pass the list of video embeds to the template
            template_values = {"logouturl": logout, "embeds": embeds}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
