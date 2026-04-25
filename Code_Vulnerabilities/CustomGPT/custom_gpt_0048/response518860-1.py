
from django.http import JsonResponse
from django.views import View

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = request.POST.get('ownerName')
            # ... other fields
            rental.save()

            return JsonResponse({'pk-user': rental.slug})
        return JsonResponse({'error': 'Invalid request'}, status=400)
