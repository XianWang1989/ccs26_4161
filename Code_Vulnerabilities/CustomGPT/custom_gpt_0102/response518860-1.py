
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental_slug = self.kwargs['slug']
            try:
                rental = Rental.objects.get(slug=rental_slug)
                rental.ownerName = request.POST.get('ownerName')
                # ...other fields...
                rental.save()
                response = HttpResponse('')
                response['pk-user'] = rental.slug
                return response
            except Rental.DoesNotExist:
                return HttpResponseNotFound('Rental not found')

        return HttpResponseRedirect('/')
