
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Code to update rental fields
            rental.save()
            response = HttpResponse('')
            response['pk-user'] = rental.slug  # Set the slug correctly
            print('response slug', response['pk-user'])
            return response
        return HttpResponseRedirect('/')
