
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            rental.ownerName = request.POST.get('ownerName')
            # Assign other fields...
            rental.save()

            response = HttpResponse('')
            response['pk-user'] = rental.slug  # Ensure 'slug' is set correctly
            print('response slug', rental.slug)  # Check slug value
            return response

        return HttpResponseRedirect('/')
