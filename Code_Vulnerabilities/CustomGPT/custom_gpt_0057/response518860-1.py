
# views.py
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
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
            response = HttpResponse('')
            response['pk-user'] = rental.slug
            print('response slug', response)
            return response
        return HttpResponseRedirect('/')

# ajax code
$.ajax({
    url: '/edit/space/' + this.props.slug + '/',
    contentType: "application/x-www-form-urlencoded",
    data: sendData,
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
    },
    error: function(xhr, status, error) {
        console.error('Error occurred:', status, error);
    }
});
