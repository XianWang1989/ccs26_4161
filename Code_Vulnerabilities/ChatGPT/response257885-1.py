
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list of YouTube embed links from the fetched suggestions
            embed_links = []
            for i in classicallist:
                link = i.link
                # Truncate the URL to get the video ID
                embed_id = link.split('/')[-1]  # Assuming format is 'https://youtu.be/VIDEO_ID'
                embed_links.append(embed_id)

            template_values = {"logouturl": logout, "links": embed_links}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
