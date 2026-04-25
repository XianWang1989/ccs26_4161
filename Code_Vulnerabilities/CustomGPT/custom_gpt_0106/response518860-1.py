
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post')
            response = HttpResponse('')
            # Extract and save fields
            try:
                rental = Rental.objects.get(slug=self.kwargs['slug'])
                rental.ownerName = request.POST.get('ownerName')
                # ... (other fields)
                rental.save()
                response['pk-user'] = rental.slug  # Ensure slug is sent back
            except Rental.DoesNotExist:
                print('Rental not found.')
                return HttpResponseBadRequest('Rental not found.')

            return response

        return HttpResponseRedirect('/')

class EditImage(View):
    def post(self, request, *args, **kwargs):
        try:
            rental = Rental.objects.get(slug=self.kwargs['slug'])
            print('Editing images for rental:', rental.slug)
        except Rental.DoesNotExist:
            return HttpResponseNotFound('Rental space not found.')

        if request.FILES:
            for file in request.FILES.getlist('image'):
                print('File:', file)
                Gallery.objects.create(rental=rental, image=file)
        return HttpResponseRedirect('/')
