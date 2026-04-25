
def post(self, request, *args, **kwargs):
    slug = self.kwargs['slug']
    try:
        rental = Rental.objects.get(slug=slug)
        # Continue processing...
    except Rental.DoesNotExist:
        return JsonResponse({'error': 'Rental not found'}, status=404)
