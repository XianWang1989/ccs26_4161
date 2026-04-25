
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = request.POST.get('ownerName')
            # Set other fields...
            rental.save()
            response_data = {'slug': rental.slug}
            print('response slug', response_data)
            return JsonResponse(response_data)

        return JsonResponse({'error': 'Invalid request'}, status=400)
