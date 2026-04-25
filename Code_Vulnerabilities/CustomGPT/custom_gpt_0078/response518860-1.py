
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse('')
            slug = self.kwargs['slug']  # Correctly fetch the slug
            rental = Rental.objects.get(slug=slug)
            # Updating rental fields...
            rental.save()

            response['pk-user'] = rental.slug  # Return the updated slug
            return response
        return HttpResponseRedirect('/')
