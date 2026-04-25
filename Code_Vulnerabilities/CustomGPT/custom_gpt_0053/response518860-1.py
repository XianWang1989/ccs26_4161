
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        if request.POST:
            response = HttpResponse('')
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            # Update rental fields…
            rental.save()
            response['pk-user'] = rental.slug
            return response

        return HttpResponse(status=400)  # Bad request if POST is not valid
