
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            response = JsonResponse({'slug': None})  # Return JSON response
            rental = Rental.objects.get(slug=self.kwargs['slug'])

            rental.ownerName = request.POST.get('ownerName')
            rental.email = request.POST.get('email')
            # Other assignments...
            rental.save()

            response['slug'] = rental.slug  # Set the slug in the response
            print('response slug', response['slug'])
            return response
        return JsonResponse({'error': 'Invalid request'}, status=400)
