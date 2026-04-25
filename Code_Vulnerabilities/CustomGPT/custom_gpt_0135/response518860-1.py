
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse('')
            # Change 'objetcs' to 'objects' (note the typo)
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Assign fields here...
            rental.save()
            response['pk-user'] = rental.slug  # Ensure this line sets a valid slug
            print('response slug', response)
            return response

        return HttpResponseRedirect('/')
