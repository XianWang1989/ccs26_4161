
class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()
        print("in FormViewA")  # This line gets executed when the super method is called
        return super(FormViewA, self).form_valid(form)  # Calls the parent class's form_valid


class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")  # This line executes first
        return super(FormViewB, self).form_valid(form)  # Calls FormViewA's form_valid
