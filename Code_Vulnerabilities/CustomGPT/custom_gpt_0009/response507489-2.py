
class FormViewB(FormViewA):
    def form_valid(self, form):
        # Execute your logic here
        form.save()
        print("in FormViewB")
        # Do not call the super method so FormViewA's method is not executed
        return HttpResponseRedirect(self.get_success_url())  # Redirect manually
