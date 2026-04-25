
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        print('Request POST data:', request.POST)

        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Update fields
            rental.ownerName = request.POST.get('ownerName')
            rental.email = request.POST.get('email')
            rental.price = request.POST.get('price')
            rental.save()
            print('Saved rental:', rental)

            response = HttpResponse('')
            response['pk-user'] = rental.slug
            print('Response slug:', response['pk-user'])
            return response

        return HttpResponseRedirect('/')

class EditImage(View):
    def post(self, request, *args, **kwargs):
        rental_slug = self.kwargs['slug']
        try:
            rental = Rental.objects.get(slug=rental_slug)
            print('Rental found:', rental)
        except Rental.DoesNotExist:
            return HttpResponseNotFound('Rental space not found')

        if request.FILES:
            for file in request.FILES.getlist('image'):
                Gallery.objects.create(rental=rental, image=file)
        return HttpResponseRedirect('/')
