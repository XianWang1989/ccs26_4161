
class ClassicalPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to hold video links
            embeds = []
            for i in classicallist:
                link = i.link
                # Extract the video ID and create the embed URL
                video_id = link.split('v=')[-1]
                if '&' in video_id:
                    video_id = video_id.split('&')[0]
                embed_url = f"https://www.youtube.com/embed/{video_id}"
                embeds.append(embed_url)

            # Prepare template values with a list of embeds
            template_values = {
                "logouturl": logout,
                "links": embeds  # Pass the list of links to the template
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
