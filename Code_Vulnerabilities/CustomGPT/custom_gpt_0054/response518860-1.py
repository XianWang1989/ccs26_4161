
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print ('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse('')
            response['pk-user'] = None

            # Ensure you're getting slug from kwargs not POST
            slug = self.kwargs.get('slug')
            if slug:
                try:
                    rental = Rental.objects.get(slug=slug)
                except Rental.DoesNotExist:
                    return HttpResponseNotFound('Rental not found')

                rental.ownerName = request.POST.get('ownerName')
                # Set other properties the same way...
                rental.save()
                response['pk-user'] = rental.slug  # Send the slug back
                print('response slug', response['pk-user']);
            return response

        return HttpResponseRedirect('/')
