
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.method == 'POST':
            print('request.post')
            print('POST data:', request.POST)
            # Check slug
            slug = self.kwargs.get('slug')
            print('slug:', slug)
            # Check if slug is valid
            try:
                rental = Rental.objects.get(slug=slug)
                # Proceed with updating fields
                # ... (existing code for updating)
                response['pk-user'] = rental.slug
                return response
            except Rental.DoesNotExist:
                print('Rental not found for slug:', slug)
                return HttpResponseBadRequest('Rental not found.')

        return HttpResponseRedirect('/')
