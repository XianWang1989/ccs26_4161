
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')  # Retrieve slug from URL
        print('Slug received:', slug)
        if not slug:
            return HttpResponseBadRequest("Slug is required")

        rental = Rental.objects.get(slug=slug)  # Use the slug
        # Update fields...
        if request.POST:
            print('Editing rental:', rental)
            # Save rental logic...
            return response

class EditImage(View):
    def post(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        try:
            rental = Rental.objects.get(slug=slug)
            print('Rental found:', rental)
        except Rental.DoesNotExist:
            return self.render(request, 'rentals/rent_detail.html', {'message': 'Rental not found'})
        # Handle file uploads...
