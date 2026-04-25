
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        print('POST data:', request.POST)

        if request.POST:
            print('request.post')
            response = HttpResponse('')
            rental_slug = self.kwargs['slug']
            rental = Rental.objects.get(slug=rental_slug)

            rental.ownerName = request.POST.get('ownerName')
            # ... other fields as above ...

            rental.save()
            response['pk-user'] = rental.slug
            print('Edited Rental Slug:', rental.slug)
            return response

        return HttpResponseRedirect('/')
