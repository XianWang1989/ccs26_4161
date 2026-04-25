
class FormViewA(FormView):
    def form_valid(self, form):
        # Base behavior
        print "in FormViewA"
        call_parent_form_valid()
        return response

class FormViewB(FormViewA):
    def form_valid(self, form):
        # Derived behavior
        print "in FormViewB"
        call_parent_form_valid()
        return response
