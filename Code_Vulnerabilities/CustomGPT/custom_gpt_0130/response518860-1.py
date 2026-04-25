
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)

        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            if rental:
                rental.ownerName = request.POST.get('ownerName')
                # ... update other fields ...
                rental.save()

                response = HttpResponse('')
                response['pk-user'] = rental.slug
                print('response slug', response['pk-user'])
                return response

        return HttpResponseRedirect('/')  # Consider modifying this to handle errors
