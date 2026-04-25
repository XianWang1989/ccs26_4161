
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical_entries = suggestions.query(suggestions.genre == "classical").order(-suggestions.date).fetch(4)

            # Create a list to hold the embedded links
            embed_links = []
            for entry in classical_entries:
                link = entry.link
                # Extract the video ID from the URL (assuming link is in the format: https://youtu.be/VIDEO_ID)
                video_id = link.split('/')[-1] if 'youtu.be' in link else link.split('v=')[-1]
                embed_links.append(video_id)

            # Prepare the template values
            template_values = {"logouturl": logout, "embed_links": embed_links}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
