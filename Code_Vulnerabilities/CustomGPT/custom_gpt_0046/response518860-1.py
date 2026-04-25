
from django.http import JsonResponse

class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)

        if request.method == 'POST':
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # ... update rental fields ...

            rental.save()
            return JsonResponse({'pk-user': rental.slug})

        return HttpResponseRedirect('/')


class EditImage(View):
    def post(self, request, *args, **kwargs):
        try:
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            print('rental slug', rental)
        except Rental.DoesNotExist:
            return JsonResponse({'message': 'Rental space not found'}, status=404)

        if request.FILES:
            for file in request.FILES.getlist('image'):
                print('file', file)
                Gallery.objects.create(rental=rental, image=file)
                print('image', file)  # Debugging line
        return JsonResponse({'status': 'success'})
