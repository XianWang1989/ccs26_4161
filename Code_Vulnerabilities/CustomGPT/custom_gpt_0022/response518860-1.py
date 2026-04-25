
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        if request.POST:
            response = HttpResponse('')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Update rental properties
            rental.ownerName = request.POST.get('ownerName')
            # Add other properties similarly...
            rental.save()
            response['pk-user'] = rental.slug  # Ensure this is set
            return response

        return HttpResponseRedirect('/')

class EditImage(View):
    def post(self, request, *args, **kwargs):
        try:
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            for file in request.FILES.getlist('image'):
                Gallery.objects.create(rental=rental, image=file)
        except Rental.DoesNotExist:
            return render(request, 'rentals/rent_detail.html', {'message': 'Rental space not found'})
        return HttpResponseRedirect('/')
