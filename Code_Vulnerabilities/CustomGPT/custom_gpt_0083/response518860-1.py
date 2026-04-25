
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse()
            # Updating rental object
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = request.POST.get('ownerName')
            # ... other fields
            rental.save()
            response['pk-user'] = rental.slug  # Ensure it's set properly
            return response
        return HttpResponseRedirect('/')
