
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # (Set all properties as before)
            # Example for clarity, other properties should also be set similarly
            rental.ownerName = request.POST.get('ownerName')
            rental.save()

            # Return JSON response instead of HttpResponse
            response_data = {
                'slug': rental.slug,  # return the slug you want to use for subsequent AJAX calls
            }
            return JsonResponse(response_data)  # Sends response back in JSON format
        return HttpResponseRedirect('/')
