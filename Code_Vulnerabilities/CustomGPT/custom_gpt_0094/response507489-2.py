
class FormViewB(FormViewA):
    def form_valid(self, form):
        # This overrides the form_valid method from FormViewA
        form.save()
        print("in FormViewB")  # Logs the message for debugging
        return super().form_valid(form)  # Calls the parent class's form_valid
