
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to hold the embedded links
            embedded_links = []
            for i in classicallist:
                link = i.link
                # Extract the video ID from the YouTube link
                video_id = link.split('v=')[1].split('&')[0]  # Get the video ID
                embed_url = f"https://www.youtube.com/embed/{video_id}"
                embedded_links.append(embed_url)

            template_values = {"logouturl": logout, "embedded_links": embedded_links}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
