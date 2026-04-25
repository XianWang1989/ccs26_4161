
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('Request Method:', request.method)
        if request.POST:
            print('POST data:', request.POST)
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            ...
            response = HttpResponse()
            response['pk-user'] = rental.slug
            return response  # Ensure this is executed
        return HttpResponseBadRequest("Invalid POST request")
