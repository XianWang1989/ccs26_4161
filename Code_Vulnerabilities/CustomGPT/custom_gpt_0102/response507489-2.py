
def form_valid(self, form):
    form.save()
    print("in FormViewB")
    # No call to super(), so FormViewA's form_valid won't run
    return super(FormViewB, self).form_valid(form)  # Optional or can be removed to skip FormViewA
