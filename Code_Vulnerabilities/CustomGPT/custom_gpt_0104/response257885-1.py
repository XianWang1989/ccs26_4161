
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            embed_links = []
            for i in classicallist:
                link = i.link
                embed = link.split('v=')[-1]  # To get the video ID
                embed_link = f"https://www.youtube.com/embed/{embed}"
                embed_links.append(embed_link)

            # Prepare template values with all video links
            template_values = {
                "logouturl": logout,
                "video_links": embed_links
            }
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
