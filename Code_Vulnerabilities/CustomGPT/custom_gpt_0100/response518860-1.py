
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse('')
            print('edited owner name is', request.POST.get('ownerName'))

            # Debug: Check slug
            slug = self.kwargs.get('slug')
            if not slug:
                print("No slug found in kwargs")
                return HttpResponseBadRequest("Slug not found")

            try:
                rental = Rental.objects.get(slug=slug)
            except Rental.DoesNotExist:
                print("Rental not found for slug:", slug)
                return HttpResponseNotFound("Rental not found")

            # Update the rental properties
            rental.ownerName = request.POST.get('ownerName')
            rental.email = request.POST.get('email')
            # ... (updating other fields)
            rental.save()
            response['pk-user'] = rental.slug
            print('response slug', response)
            return response

        return HttpResponseRedirect('/')
