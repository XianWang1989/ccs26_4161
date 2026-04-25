
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')  # This line should log if request.POST exists
            response = HttpResponse('')
            # ... existing code to update the rental

            # Assuming you've successfully saved the rental object
            response['pk-user'] = rental.slug  # Ensure this part executes correctly
            print('response slug', response['pk-user'])  # Print to debug the slug
            return response

        return HttpResponseRedirect('/')
