
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        if request.POST:
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Update fields...
            rental.save()
            return JsonResponse({'slug': rental.slug}, status=200)  # Use JsonResponse here
        return JsonResponse({'error': 'Invalid request'}, status=400)
