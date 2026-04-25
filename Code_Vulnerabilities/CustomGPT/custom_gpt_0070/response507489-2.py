
class FormViewC(FormViewB):
    def get_success_url(self):
        # Custom success URL logic
        return reverse('another_url')
