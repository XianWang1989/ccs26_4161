
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to hold the embedded video links
            embeds = []
            for i in classicallist:
                link = i.link
                # Truncate the YouTube URL for embedding
                embed = link.split('v=')[1] if 'v=' in link else link
                embeds.append(embed)

            template_values = {"logouturl": logout, "links": embeds}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
