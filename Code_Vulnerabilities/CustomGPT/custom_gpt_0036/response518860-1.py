
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.method == "POST":
            print('request.post')
            # Check received data
            if not request.POST:
                return JsonResponse({'error': 'No POST data received'}, status=400)

            slug = kwargs.get('slug')
            rental = Rental.objects.get(slug=slug)
            # Update rental properties...

            response = HttpResponse('')
            response['pk-user'] = rental.slug
            print('response slug', response)
            return response

        return HttpResponseRedirect('/')
