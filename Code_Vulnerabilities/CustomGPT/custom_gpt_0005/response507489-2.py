
def form_valid(self, form):
    form.save()
    print("in FormViewB")
    # comment out the super call to skip FormViewA's method
    # return super(FormViewB, self).form_valid(form)
    return HttpResponseRedirect(self.get_success_url())
