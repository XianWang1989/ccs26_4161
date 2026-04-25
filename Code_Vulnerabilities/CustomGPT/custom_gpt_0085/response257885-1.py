
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to hold the embedded links
            embed_links = []
            for i in classicallist:
                link = i.link
                # Extract the video ID from the share URL
                video_id = link.split("v=")[-1]
                # Construct the embed link
                embed_link = f"https://www.youtube.com/embed/{video_id}"
                embed_links.append(embed_link)

            # Prepare template values
            template_values = {
                "logouturl": logout,
                "embed_links": embed_links
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
