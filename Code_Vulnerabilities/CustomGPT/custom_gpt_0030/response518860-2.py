
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        if request.POST:
            response_data = {
                "slug": request.POST.get('slug')
            }
            # Save the rental properties
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = request.POST.get('ownerName')
            # ... (set other properties)
            rental.save()
            response_data['pk-user'] = rental.slug
            return JsonResponse(response_data)  # Use JsonResponse here
