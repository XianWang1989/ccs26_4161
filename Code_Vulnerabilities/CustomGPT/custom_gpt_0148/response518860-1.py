
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post received')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Update rental details...
            rental.save()
            response = HttpResponse('')
            response['pk-user'] = rental.slug  # Ensure slug is set here
            print('response slug', response['pk-user'])
            return response
        return HttpResponseRedirect('/')
