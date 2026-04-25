
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
                # Extract the video ID from the link. For example, handle 'https://youtu.be/VIDEO_ID'
                video_id = link.split('/')[-1] if 'youtu.be' in link else link.split('v=')[-1]
                embeds.append(video_id)

            # Prepare template values, mapping each embed to a specific iframe
            template_values = {
                "logouturl": logout,
                "embeds": embeds  # Pass the list of video IDs to the template
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
