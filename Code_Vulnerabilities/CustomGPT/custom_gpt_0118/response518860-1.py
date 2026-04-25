
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.body:  # Change to check request body
            print('request.body:', request.body)
            data = json.loads(request.body)
            # Handle your data as needed from `data`
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = data.get('ownerName')
            # ... (set other properties similarly)
            rental.save()
            response = HttpResponse('')
            response['pk-user'] = rental.slug
            return response

        return HttpResponseRedirect('/')
