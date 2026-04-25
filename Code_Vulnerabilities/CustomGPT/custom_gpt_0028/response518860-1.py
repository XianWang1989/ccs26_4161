
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse('')
            rental_slug = self.kwargs.get('slug')
            try:
                rental = Rental.objects.get(slug=rental_slug)
            except Rental.DoesNotExist:
                return HttpResponse('Rental not found', status=404)

            # Update rental properties
            rental.ownerName = request.POST.get('ownerName')
            # ... update other fields
            rental.save()
            response['pk-user'] = rental.slug  # Ensure the slug is set
            print('response slug', response['pk-user'])
            return response
        return HttpResponseRedirect('/')
