
class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()
        print("in FormViewA")  # This gets executed from FormViewB
        return super().form_valid(form)


class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")  # This executes first
        return super().form_valid(form)
