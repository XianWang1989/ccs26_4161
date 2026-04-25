
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        if request.POST:
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Update rental attributes
            rental.save()
            response = HttpResponse('')
            response['pk-user'] = rental.slug  # Ensure this is set correctly
            return response
        return HttpResponseRedirect('/')
