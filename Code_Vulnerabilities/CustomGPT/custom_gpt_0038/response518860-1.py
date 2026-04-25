
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse('')
            slug = self.kwargs['slug']
            rental = Rental.objects.get(slug=slug)  # Check slug is valid
            rental.ownerName = request.POST.get('ownerName')
            rental.save()
            response['pk-user'] = rental.slug  # Ensure slug is set
            print('response slug', response['pk-user'])
            return response

        return HttpResponseRedirect('/')
