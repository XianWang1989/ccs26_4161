
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            rental = Rental.objects.get(slug=self.kwargs['slug'])

            # Update rental details
            rental.ownerName = request.POST.get('ownerName')
            #... (other fields) ...

            rental.save()
            response = HttpResponse('')
            response['pk-user'] = rental.slug  # Ensure this is set correctly
            return response

        return HttpResponseRedirect('/')
