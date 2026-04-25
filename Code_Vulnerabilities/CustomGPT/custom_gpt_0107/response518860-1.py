
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental_slug = self.kwargs['slug']  # Capture the slug from kwargs
            print('rental slug', rental_slug)

            try:
                rental = Rental.objects.get(slug=rental_slug)
            except Rental.DoesNotExist:
                return HttpResponseBadRequest('Rental not found')

            # Update fields
            rental.ownerName = request.POST.get('ownerName')
            rental.email = request.POST.get('email')
            # ... (other fields)
            rental.save()

            response = HttpResponse('')
            response['pk-user'] = rental.slug  # Ensure this is set
            print('response slug', response['pk-user'])
            return response

        return HttpResponseRedirect('/')
