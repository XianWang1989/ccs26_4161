
class classicalpage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            logout = users.create_logout_url(self.request.uri)
            classical = suggestions.query(suggestions.genre == "classical").order(-suggestions.date)
            classicallist = classical.fetch(4)

            # Create a list to store the embedded video links
            embed_links = []

            for i in classicallist:
                link = i.link
                # Truncate and prepare the embed link
                embed = link.split("v=")[1] if "v=" in link else link
                embed_links.append(embed)

            template_values = {"logouturl": logout, "embed_links": embed_links}
            template = JINJA_ENVIRONMENT.get_template("classical.html")
            self.response.write(template.render(template_values))
        else:
            self.redirect("/")
