
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.body:  # This checks if there is a request body
            print('request.post')
            data = json.loads(request.body)  # Load the JSON body
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = data.get('ownerName')
            # ... continue with updating other fields
            rental.save()
            return JsonResponse({'slug': rental.slug})  # Return JSON response

        return HttpResponseRedirect('/')
