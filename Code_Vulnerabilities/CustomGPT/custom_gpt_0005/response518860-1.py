
import json

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.body:  # Check if the body is being read
            data = json.loads(request.body.decode('utf-8'))
            print('request.post', data)

            # Ensure slug is correctly fetched
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = data.get('ownerName')
            # ... (update other fields)
            rental.save()

            response = HttpResponse('')
            response['pk-user'] = rental.slug
            print('response slug', response)
            return response

        return HttpResponseRedirect('/')
