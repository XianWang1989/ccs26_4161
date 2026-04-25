
class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")
        # Comment this out to prevent calling FormViewA's form_valid
        # return super(FormViewB, self).form_valid(form)  
        return HttpResponseRedirect(self.get_success_url())  # Or your custom logic
