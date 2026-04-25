
def form_valid(self, form):
    form.save()  # Custom behavior for FormViewB
    print("in FormViewB")
    return super(FormViewB, self).form_valid(form)  # Calls FormViewA's form_valid
