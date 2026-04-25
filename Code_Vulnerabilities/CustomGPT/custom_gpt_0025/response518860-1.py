
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse('')
            print('edited owner name is', request.POST.get('ownerName'))

            # Ensure slug is fetched from kwargs
            slug = self.kwargs['slug']
            rental = Rental.objects.get(slug=slug)
            rental.ownerName = request.POST.get('ownerName')
            # Other fields...

            rental.save()
            response['pk-user'] = rental.slug  # Set to correct slug
            print('response slug', response['pk-user'])
            return response

        return HttpResponseRedirect('/')
