
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Prepare a list of embed links
            embed_links = []
            for i in classicallist:
                link = i.link
                # Extract video ID (assuming the link is in the format: https://youtu.be/VIDEO_ID)
                video_id = link.split('/')[-1]  # Adjust depending on the exact URL format
                embed_links.append(video_id)

            template_values = {"logouturl": logout, "embed_links": embed_links}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
