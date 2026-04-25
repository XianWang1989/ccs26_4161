
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        if request.POST:
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = request.POST.get('ownerName')
            # Update other fields...
            rental.save()
            return JsonResponse({'slug': rental.slug})

        return JsonResponse({'error': 'Invalid request'}, status=400)
