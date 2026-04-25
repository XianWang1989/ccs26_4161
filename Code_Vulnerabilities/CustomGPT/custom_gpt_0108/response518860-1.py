
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse('')
            rental = Rental.objects.get(slug=self.kwargs['slug'])  # Corrected this line
            # ... [other processing]
            response['pk-user'] = rental.slug
            print('response slug', response)
            return response
        return HttpResponseRedirect('/')
