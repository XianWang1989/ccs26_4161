
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to hold the embedded video URLs
            video_links = []
            for i in classicallist:
                link = i.link
                embed = link.split('/')[-1]  # Extract the video ID
                video_links.append(embed)  # Collect the video IDs

            # Template context needs to hold the video links list
            template_values = {"logouturl": logout, "video_links": video_links}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
