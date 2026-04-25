
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Updating rental fields
            rental.ownerName = request.POST.get('ownerName')
            # ... (other fields)
            rental.save()
            return JsonResponse({'slug': rental.slug})  # Ensure a JSON response is sent

        return HttpResponse(status=400)  # Bad request if POST data is missing
