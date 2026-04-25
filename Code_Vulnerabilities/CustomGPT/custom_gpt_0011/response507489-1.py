
class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()
        print("in FormViewA")  # Use parentheses for print function
        return super(FormViewA, self).form_valid(form)

class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")  # Use parentheses for print function
        # Do not call super() if you do not want to execute FormViewA's logic.

        # Instead, return a specific response if needed
        return self.get_success_url()  # Or any other logic to handle success
