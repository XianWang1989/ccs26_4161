
class EditSpaceView(View):
    def post(self, request, *args, **kwargs):
        print('edit space view', request)
        if request.POST:
            print('request.post', request.POST)
            try:
                rental = Rental.objects.get(slug=self.kwargs['slug'])
                # Update code here...
                return JsonResponse({'pk-user': rental.slug})
            except Rental.DoesNotExist:
                return JsonResponse({'error': 'Rental not found'}, status=404)

        return HttpResponseRedirect('/')
