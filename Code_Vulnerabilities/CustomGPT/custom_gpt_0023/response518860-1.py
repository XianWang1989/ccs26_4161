
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)

        if request.POST:
            print('request.post')
            response = HttpResponse('')

            try:
                rental = Rental.objects.get(slug=self.kwargs['slug'])
                rental.ownerName = request.POST.get('ownerName')
                # ... update other fields as before
                rental.save()
                response['pk-user'] = rental.slug
            except Rental.DoesNotExist:
                return HttpResponse(status=404)

            print('response slug', response['pk-user'])
            return response

        return HttpResponseRedirect('/')
