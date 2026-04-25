
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Collect each video link
            embed_links = []
            for i in classicallist:
                link = i.link
                # Extract the video ID and append to list
                video_id = link.split('v=')[1].split('&')[0]  # Get the video ID
                embed_links.append(video_id)

            # Prepare template values with individual links
            template_values = {"logouturl": logout, "embed_links": embed_links}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
