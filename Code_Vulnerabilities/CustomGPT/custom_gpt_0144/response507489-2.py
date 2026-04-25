# Parent class
class FormViewA(FormView):
    def form_valid(self, form):
        print("FormViewA: Validating form")
        return super().form_valid(form)

# Child class
class FormViewB(FormViewA):
    def form_valid(self, form):
        print("FormViewB: Validating form")
        return super().form_valid(form)  # Calls FormViewA's form_valid()

# Usage:
# When form is valid, output will be:
# FormViewB: Validating form
# FormViewA: Validating form
