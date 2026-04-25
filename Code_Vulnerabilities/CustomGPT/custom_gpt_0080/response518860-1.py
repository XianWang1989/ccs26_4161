
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Update rental details
            rental.ownerName = request.POST.get('ownerName')
            # ... (update other fields)
            rental.save()

            response = JsonResponse({'pk-user': rental.slug})  # Return slug as JSON
            print('response slug', response)
            return response
        return HttpResponseRedirect('/')
