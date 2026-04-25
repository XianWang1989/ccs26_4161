
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Update rental fields...
            rental.save()
            response = HttpResponse('')
            response['pk-user'] = rental.slug  # Ensure slug is correctly set
            print('response slug', response['pk-user'])
            return response

        return HttpResponseRedirect('/')
