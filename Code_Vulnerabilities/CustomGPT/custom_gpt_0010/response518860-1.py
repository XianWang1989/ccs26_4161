
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            slug = self.kwargs.get('slug')
            print('retrieved slug:', slug)
            if slug is None:
                return HttpResponseBadRequest("Slug not provided.")

            rental = Rental.objects.get(slug=slug)
            # Continue with updating fields...
