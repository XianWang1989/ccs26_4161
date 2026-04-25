
class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")
        # Do not call super() to skip FormViewA's form_valid
        return self.get_success_url()
