
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        if request.POST:
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Update rental details
            rental.ownerName = request.POST.get('ownerName')
            # ... (other fields)
            rental.save()

            # Return the updated slug in response headers
            response = HttpResponse('')
            response['pk-user'] = rental.slug
            return response
        return HttpResponseRedirect('/')
