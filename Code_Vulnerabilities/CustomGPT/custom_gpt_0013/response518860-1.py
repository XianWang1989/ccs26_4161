
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            slug = self.kwargs['slug']  # Ensure you're getting the slug correctly
            try:
                rental = Rental.objects.get(slug=slug)
            except Rental.DoesNotExist:
                return HttpResponse('Rental not found', status=404)

            # Updating rental properties...
            rental.ownerName = request.POST.get('ownerName')
            # (Include all other fields similarly)
            rental.save()
            response = HttpResponse('')
            response['pk-user'] = rental.slug
            print('response slug', response)
            return response
        return HttpResponseRedirect('/')
