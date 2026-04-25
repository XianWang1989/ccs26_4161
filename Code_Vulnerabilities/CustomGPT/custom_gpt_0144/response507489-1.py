class FormViewA(FormView):
    form_class = MyFormClass
    template_name = 'mytemplate.html'

    def get_success_url(self):
        return reverse('my_url')

    def form_valid(self, form):
        form.save()
        print("in FormViewA")
        return super(FormViewA, self).form_valid(form)


class FormViewB(FormViewA):
    def form_valid(self, form):
        form.save()
        print("in FormViewB")
        # Remove the super() call if you don't want FormViewA's form_valid to run
        return HttpResponseRedirect(self.get_success_url())
