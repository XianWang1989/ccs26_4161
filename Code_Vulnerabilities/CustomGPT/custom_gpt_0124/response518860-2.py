
if request.is_ajax():
    return JsonResponse({'slug': rental.slug})
else:
    return HttpResponseRedirect('/')
