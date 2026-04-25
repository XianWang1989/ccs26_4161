
class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        # This is executed when the form is valid.
        form.save()
        print("in FormViewA")  # Logs a message for debugging
        return super().form_valid(form)  # Call the parent implementation
