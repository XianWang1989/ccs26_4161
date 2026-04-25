
from django.views import View
from django.http import JsonResponse
import json

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        try:
            data = json.loads(request.body)  # Parse JSON body
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = data.get('ownerName')
            # Update other fields similarly...
            rental.save()
            response_data = {'pk-user': rental.slug}
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

