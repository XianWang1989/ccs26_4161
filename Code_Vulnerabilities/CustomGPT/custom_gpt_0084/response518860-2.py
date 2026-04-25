
class EditImage(View):
    def post(self, request, *args, **kwargs):
        try:
            rental = Rental.objects.get(slug=self.kwargs['slug'])
        except Rental.DoesNotExist:
            return JsonResponse({'error': 'Rental space not found'}, status=404)

        if request.FILES:
            for file in request.FILES.getlist('image'):
                Gallery.objects.create(rental=rental, image=file)
        return JsonResponse({'status': 'success'})
