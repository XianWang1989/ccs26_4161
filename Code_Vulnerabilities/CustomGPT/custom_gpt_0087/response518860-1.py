
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            response = HttpResponse()
            slug = self.kwargs.get('slug')
            rental = Rental.objects.get(slug=slug)

            for field in ['ownerName', 'email', 'phoneNumber', 'listingName', 'summary', 'property', 'room', 'price', 'city', 'place', 'water', 'amenities']:
                setattr(rental, field, request.POST.get(field))
            rental.save()

            response['pk-user'] = rental.slug  # Use rental.slug instead of a null slug
            print('response slug', response)
            return response

        return HttpResponseRedirect('/')
