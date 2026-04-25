
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.POST:', request.POST)  # Debug the incoming POST data
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Update rental attributes here...
            rental.save()
            response = HttpResponse('')
            response['pk-user'] = rental.slug
            return response
        return HttpResponseRedirect('/')
