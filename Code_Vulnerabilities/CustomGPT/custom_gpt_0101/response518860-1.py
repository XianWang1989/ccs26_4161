
# Adjust your view to ensure slug is correctly passed.

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse('')
            # Ensure slug is retrieved correctly
            slug = self.kwargs['slug']
            print('slug for rental:', slug)
            try:
                rental = Rental.objects.get(slug=slug)
            except Rental.DoesNotExist:
                return HttpResponseNotFound('Rental not found')

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
            print('response slug', response)
            return response

        return HttpResponseRedirect('/')

# Ensure that your AJAX call sends the slug correctly and check for success.

$.ajax({
    url: '/edit/space/' + this.props.slug + '/',
    contentType: "application/json",
    data: JSON.stringify(sendData),  # Send as JSON
    type: 'POST',
    success: function(data, textStatus, xhr) {
        console.log('rent worked');
        var slug = xhr.getResponseHeader('pk-user');
        console.log('slug', slug);
        $.ajax({
            url: '/edit/image/' + slug + '/',
            data: image,
            contentType: false,
            processData: false,
            type: 'POST',
            success: function(data) {
                console.log('success');
            }
        });
    }
});
