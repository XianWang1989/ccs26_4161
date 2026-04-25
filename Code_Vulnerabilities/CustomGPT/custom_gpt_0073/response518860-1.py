
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.body:  # Use request.body for JSON data
            data = json.loads(request.body)
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = data.get('ownerName')
            # Continue assigning other fields...
            rental.save()
            response = HttpResponse('')
            response['pk-user'] = rental.slug
            return response
        return HttpResponseRedirect('/')
