
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        if request.POST:
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Update fields
            rental.ownerName = request.POST.get('ownerName')
            rental.email = request.POST.get('email')
            # ... update other fields ...
            rental.save()
            return JsonResponse({'slug': rental.slug, 'status': 'success'})

        return JsonResponse({'status': 'failed'})
