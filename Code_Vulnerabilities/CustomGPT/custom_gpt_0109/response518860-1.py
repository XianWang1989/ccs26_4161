
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        if request.POST:
            slug = self.kwargs['slug']
            try:
                rental = Rental.objects.get(slug=slug)
                rental.ownerName = request.POST.get('ownerName')
                # (Set other fields similarly)
                rental.save()
                return JsonResponse({'pk-user': rental.slug})  # Return JSON response
            except Rental.DoesNotExist:
                return JsonResponse({'error': 'Rental not found'}, status=404)
        return JsonResponse({'error': 'Invalid request'}, status=400)
