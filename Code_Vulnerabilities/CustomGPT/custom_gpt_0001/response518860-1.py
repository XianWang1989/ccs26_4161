
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse('')
            rental = Rental.objects.get(slug=self.kwargs['slug'])  # Ensure you handle the possibility of this not being found

            # Update rental fields
            rental.ownerName = request.POST.get('ownerName')
            ...
            rental.save()

            response['pk-user'] = rental.slug  # Ensure this is correctly set
            print('response slug', response['pk-user'])
            return response

        return HttpResponseRedirect('/')
