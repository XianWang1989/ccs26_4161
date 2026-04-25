
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse('')
            # Capture the slug correctly
            slug = self.kwargs['slug']
            print('edited owner name is', request.POST.get('ownerName'))
            rental = Rental.objects.get(slug=slug)
            # Update rental properties
            rental.ownerName = request.POST.get('ownerName')
            # ... (additional properties)
            rental.save()
            response['pk-user'] = rental.slug # This slug should be valid now
            print('response slug', response['pk-user'])
            return response
        return HttpResponseRedirect('/')
