
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)
            video_links = []

            # Iterate through the fetched suggestions and truncate the URLs for embedding
            for i in classicallist:
                link = i.link
                embed = link.split("/")[-1]  # Extract the video ID from the URL
                video_links.append(embed)  # Add the video ID to the list

            # Pass the entire list of video links to the template
            template_values = {"logouturl": logout, "video_links": video_links}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
