
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post:', request.POST)
            rental_slug = self.kwargs['slug']
            try:
                rental = Rental.objects.get(slug=rental_slug)
                print('Rental found for slug:', rental_slug)
            except Rental.DoesNotExist:
                print('Rental not found for slug:', rental_slug)
                return HttpResponseNotFound('Rental not found')

            rental.ownerName = request.POST.get('ownerName')
            rental.email = request.POST.get('email')
            # ... other fields update ...

            rental.save()
            response = HttpResponse('')
            response['pk-user'] = rental.slug
            print('Updated rental slug:', response['pk-user'])
            return response

        return HttpResponseRedirect('/')
