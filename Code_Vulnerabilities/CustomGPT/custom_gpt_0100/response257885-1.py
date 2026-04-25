
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical_query = suggestions.query(suggestions.genre == "classical").order(-suggestions.date).fetch(4)

            # Create a list to hold embedded video URLs
            embeds = []
            for entry in classical_query:
                link = entry.link
                video_id = link.split('/')[-1]  # Extract video ID from the link
                embed_url = f"https://www.youtube.com/embed/{video_id}"
                embeds.append(embed_url)

            # Prepare the template values
            template_values = {"logouturl": logout, "embeds": embeds}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
