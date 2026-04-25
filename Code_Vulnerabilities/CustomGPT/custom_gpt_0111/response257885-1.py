
class suggestionndb(webapp2.RequestHandler):
    def post(self):
        suggestion = suggestions()
        suggestion.link = self.request.get("suggestlink")
        suggestion.genre = self.request.get("suggestgenre")
        suggestion.date = datetime.datetime.now()
        suggestion.put()
