
class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")
        # Don't call super() to prevent FormViewA's form_valid from executing
        return HttpResponseRedirect(self.get_success_url())  # Or any other logic you'd want to implement
