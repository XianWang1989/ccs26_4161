
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        if request.POST:
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Set rental attributes
            rental.save()
            response = HttpResponse('')
            response['pk-user'] = rental.slug  # Ensure slug is correctly set
            return response
        return HttpResponseRedirect('/')
