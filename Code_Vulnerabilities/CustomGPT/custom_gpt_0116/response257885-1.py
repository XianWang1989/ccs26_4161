
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            # Fetch the four most recent classical suggestions
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Prepare a list of embedded video links
            embeds = []
            for i in classicallist:
                link = i.link
                # Extract the video ID from the URL
                video_id = link.split('/')[-1].split('?v=')[-1]
                embeds.append(video_id)

            # Prepare the template values to pass to the HTML
            template_values = {"logouturl": logout, "embeds": embeds}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
