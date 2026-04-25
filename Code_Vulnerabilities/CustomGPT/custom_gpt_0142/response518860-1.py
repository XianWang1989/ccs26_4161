
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)

        # Print all POST data for debugging
        print('POST Data:', request.POST)

        if request.POST:
            ...
