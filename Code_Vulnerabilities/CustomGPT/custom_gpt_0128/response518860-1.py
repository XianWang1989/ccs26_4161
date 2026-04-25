
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.method == 'POST':
            print('request.post')
            response = HttpResponse('')
            slug = self.kwargs['slug']  # Get slug from URL parameters
            rental = Rental.objects.filter(slug=slug).first()  # Use filter to prevent DoesNotExist

            if rental:
                rental.ownerName = request.POST.get('ownerName', '')
                rental.email = request.POST.get('email', '')
                # ... update other fields
                rental.save()
                response['pk-user'] = rental.slug
                print('response slug', response['pk-user'])
                return response
            else:
                print('Rental not found for slug', slug)
        return HttpResponseRedirect('/')
