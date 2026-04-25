
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = request.POST.get('ownerName')
            # update other fields...
            rental.save()

            response = JsonResponse({'slug': rental.slug})  # Return the slug as JSON
            return response

        return HttpResponseRedirect('/')
