
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)

        if request.POST:
            print('request.post')
            rental_slug = self.kwargs.get('slug')  # Get slug from kwargs

            try:
                rental = Rental.objects.get(slug=rental_slug)
                # Update rental fields...
                rental.save()

                response = HttpResponse('')
                response['pk-user'] = rental.slug  # Ensure that 'slug' is returned
                print('response slug', response)
                return response

            except Rental.DoesNotExist:
                return HttpResponse('Rental not found', status=404)

        return HttpResponseRedirect('/')
