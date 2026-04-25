
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = JsonResponse({'status': 'success'})
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = request.POST.get('ownerName')
            # Continue updating fields...
            rental.save()
            response['pk-user'] = rental.slug  # Ensure slug is set here
            print('response slug', response['pk-user'])
            return response  # Return JSON response directly

        return JsonResponse({'status': 'error', 'message': 'Invalid request'})
