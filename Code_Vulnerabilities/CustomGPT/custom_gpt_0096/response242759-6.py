
from django.views import View
from django.shortcuts import render, redirect

class AdditionalInfoView(View):
    def get(self, request):
        return render(request, 'additional_info.html')

    def post(self, request):
        business_details = request.POST.get('business_details')
        request.user.business_details = business_details
        request.user.save()
        return redirect('some_view')
