
# views.py
from django.views.generic import UpdateView

class ArchitectDetailsView(UpdateView):
    model = get_user_model()
    template_name = 'yourapp/architect_details.html'
    fields = ['business_name', 'business_address']

    def get_object(self):
        return self.request.user
