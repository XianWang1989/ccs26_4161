
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        print('request.POST:', request.POST)  # Debug POST data

        if request.POST:
            print('request.post')
            # Your current handling logic
            try:
                rental = Rental.objects.get(slug=self.kwargs['slug'])
                # Continue your handling logic...
            except Rental.DoesNotExist:
                print('Rental with this slug does not exist!')
                return HttpResponse('No rental found', status=404)
