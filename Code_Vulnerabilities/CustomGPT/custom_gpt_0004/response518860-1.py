
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse('')
            rental = Rental.objects.get(slug=self.kwargs['slug'])

            # ... (updating rental fields)

            rental.save()
            response['pk-user'] = rental.slug  # Ensure slug is set from the rental object
            print('response slug', response['pk-user'])  # Log the slug for debugging
            return response

        return HttpResponseRedirect('/')
