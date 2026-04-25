
def get_widget_by_name(self, name):
    return self.get_child_by_name(name)

# Usage example
widget = self.get_widget_by_name("Clock1")
if widget:
    widget.set_text("Updated Time")
