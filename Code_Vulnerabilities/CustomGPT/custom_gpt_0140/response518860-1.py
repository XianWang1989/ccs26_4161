
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = request.POST.get('ownerName')
            # Add other fields as applicable
            rental.save()

            response = HttpResponse('')
            response['pk-user'] = rental.slug
            print('response slug', response)
            return response

        return HttpResponseBadRequest() # relevant for AJAX if needed
