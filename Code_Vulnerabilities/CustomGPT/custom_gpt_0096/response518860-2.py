
class EditImage(View):
    def post(self, request, *args, **kwargs):
        rental = Rental.objects.filter(slug=self.kwargs['slug']).first()
        if not rental:
            return HttpResponseNotFound('Rental not found')
        # Process file uploads...
        return HttpResponseRedirect('/')
