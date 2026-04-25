
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        # It may return 302 if the request is improperly formatted (check AJAX data)
        if request.POST:
            print('request.post')
            rental_slug = self.kwargs['slug']
            try:
                rental = Rental.objects.get(slug=rental_slug)
                # Populate rental properties
                rental.ownerName = request.POST.get('ownerName')
                # ... other fields ...
                rental.save()
                response = HttpResponse('')
                response['pk-user'] = rental.slug
                print('response slug', response)
                return response
            except Rental.DoesNotExist:
                return HttpResponse(status=404)

        return HttpResponseRedirect('/')
