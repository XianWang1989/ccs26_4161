
# views.py
class ArchitectDetailsView(FormView):
    form_class = ArchitectDetailsForm
    template_name = 'architect_details.html'

    def form_valid(self, form):
        # Save the architect details
        return super().form_valid(form)

# urls.py
urlpatterns += [
    path('architect/details/', ArchitectDetailsView.as_view(), name='architect_details'),
]
