
class Widget():
    def __init__(self, parent, name):
        print("ADDING CLOCK")
        self.gtkwidget = Gtk.Label()
        self.format = Defaults.widget.defaultClockFormat
        self.name = name + parentName
        self.gtkwidget.set_name(self.name)
        self.parent = parent  # Keep a reference to the parent

    def update(self):
        print("Setting clock text to", strftime(self.format, gmtime()))
        # Get the label by name from the parent
        child_widget = self.parent.get_widget_by_name(self.name)
        if child_widget:
            child_widget.set_text(strftime(self.format, gmtime()))
        else:
            print("Widget not found. Ensure that the widget name is correct.")

# Example of adding the widget to the parent
class Parent(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clock Example")
        self.show_all()

    def get_widget_by_name(self, name):
        return self.get_children()[0].get_name() == name  # Custom retrieval logic for your layout
