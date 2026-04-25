
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])  # Fixed typo: 'objetcs' to 'objects'
            # Updating other fields...
            rental.save()

            response = HttpResponse('')
            response['pk-user'] = rental.slug  # Ensure slug is set correctly
            return response

        return HttpResponseRedirect('/')
