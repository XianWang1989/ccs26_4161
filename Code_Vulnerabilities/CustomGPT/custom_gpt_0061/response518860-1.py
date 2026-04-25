
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.body:  # Ensure body has content
            print('request.post')
            # Additional logs can help
            print('Request body:', request.body)
            ...
