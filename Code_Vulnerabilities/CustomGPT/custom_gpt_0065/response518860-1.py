
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        slug = self.kwargs.get('slug')
        if request.POST:
            try:
                rental = Rental.objects.get(slug=slug)
            except Rental.DoesNotExist:
                return HttpResponse('Rental not found', status=404)

            print('request.post')
            print('edited owner name is', request.POST.get('ownerName'))
            rental.ownerName = request.POST.get('ownerName')
            rental.email = request.POST.get('email')
            # ... update other fields

            rental.save()
            response = HttpResponse('')
            response['pk-user'] = rental.slug
            print('response slug', response)
            return response

        return HttpResponseRedirect('/')
