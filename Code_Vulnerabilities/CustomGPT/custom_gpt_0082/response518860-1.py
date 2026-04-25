
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse('')
            slug = self.kwargs['slug']
            try:
                rental = Rental.objects.get(slug=slug)
                rental.ownerName = request.POST.get('ownerName')
                rental.email = request.POST.get('email')
                rental.phoneNumber = request.POST.get('phoneNumber')
                rental.listingName = request.POST.get('listingName')
                rental.summary = request.POST.get('summary')
                rental.property = request.POST.get('property')
                rental.room = request.POST.get('room')
                rental.price = request.POST.get('price')
                rental.city = request.POST.get('city')
                rental.place = request.POST.get('place')
                rental.water = request.POST.get('water')
                rental.amenities = request.POST.get('amenities')
                rental.save()
                response['pk-user'] = rental.slug
                return response
            except Rental.DoesNotExist:
                return HttpResponse(status=404)  # Not Found status for rental

        return HttpResponseRedirect('/')  # Handle GET/POST separately

class EditImage(View):
    def post(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        try:
            rental = Rental.objects.get(slug=slug)
            if request.FILES:
                for file in request.FILES.getlist('image'):
                    Gallery.objects.create(rental=rental, image=file)
            return HttpResponseRedirect('/')
        except Rental.DoesNotExist:
            return HttpResponse(status=404)  # Handle rental not found
