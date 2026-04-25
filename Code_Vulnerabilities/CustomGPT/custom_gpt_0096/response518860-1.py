
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.filter(slug=self.kwargs['slug']).first()
            if rental:  # Ensure rental exists
                rental.ownerName = request.POST.get('ownerName')
                # Set other fields...
                rental.save()
                response = HttpResponse('')
                response['pk-user'] = rental.slug  # Set slug in response headers
                print('response slug', response)
                return response
            else:
                return HttpResponseBadRequest('Rental not found')
        return HttpResponseRedirect('/')
