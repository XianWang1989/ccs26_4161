
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Creating a list to store the embedded links
            embed_links = []
            for i in classicallist:
                link = i.link
                # Extract the YouTube video ID from the link
                embed = link.split('v=')[1]  # Assuming the link is in the form https://www.youtube.com/watch?v=VIDEO_ID
                # Check if there are any parameters after the video ID and truncate accordingly
                if '&' in embed:
                    embed = embed.split('&')[0]
                embed_links.append(embed)

            # Prepare the template values
            template_values = {
                "logouturl": logout,
                "embed_links": embed_links  # Pass the list of links to the template
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
