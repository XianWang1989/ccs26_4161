
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')

            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = request.POST.get('ownerName')
            rental.email = request.POST.get('email')
            # update other fields...
            rental.save()

            response = HttpResponse('')
            response['pk-user'] = rental.slug  # Ensure the slug is set correctly
            print('response slug', response['pk-user'])
            return response

        return HttpResponseRedirect('/')
