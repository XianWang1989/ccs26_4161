
class EditSpaceView(View):
    def post(self,request, *args, **kwargs):
        print('edit space view', request)

        if request.POST:
            print('request.post')
            slug = self.kwargs.get('slug')  # Get slug from kwargs
            if not slug:
                return JsonResponse({'error': 'Slug is required'}, status=400)

            try:
                rental = Rental.objects.get(slug=slug)
            except Rental.DoesNotExist:
                return JsonResponse({'error': 'Rental not found'}, status=404)

            # Process the rest of your fields...
            rental.ownerName = request.POST.get('ownerName')
            # ... update the remaining fields

            rental.save()
            return HttpResponse(status=204)  # No Content, as a successful update

        return HttpResponseRedirect('/')
