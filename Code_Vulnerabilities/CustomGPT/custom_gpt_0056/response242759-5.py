
# myapp/views.py

from django.shortcuts import redirect
from django.views import View

class UserTypeView(View):
    def get(self, request):
        # Logic to choose user type
        return render(request, 'user_type_form.html')

    def post(self, request):
        user_type = request.POST.get('user_type')
        if user_type == 'arch':
            # Redirect to business details form
            return redirect('business_details')
        return redirect('home')
