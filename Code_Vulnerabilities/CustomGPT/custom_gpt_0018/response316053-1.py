
class Widget():
    def __init__(self, parent, name):
        print("ADDING CLOCK")
        self.gtkwidget = Gtk.Label()  # Create the label
        self.format = Defaults.widget.defaultClockFormat
        self.name = name + "_clock"  # Ensuring unique naming structure
        self.gtkwidget.set_name(self.name)
        self.parent = parent  # Keep a reference to parent for updates

    def update(self):
        current_time = strftime(self.format, gmtime())
        print("Setting clock text to", current_time)

        # Update the label text
        self.gtkwidget.set_text(current_time)
        self.gtkwidget.queue_draw()  # Ensure the label is redrawn

    # No need for searching, we access the widget directly
    def runCommand(self, command, lineCount, configurationFile):
        # GMTTIME TRUE OR FALSE
        print("I am about to run", command, "from inside the Clock widget!")

        if command.startswith("format="):
            parts = command.split("=")
            if len(parts) != 2:
                output.stderr(configurationFile + ", line " + str(lineCount) + ": Badly formatted command 'format': Format: format = format.\nSkipping...")
                return

            self.format = parts[1]

    def widget(self):
        return self.gtkwidget  # Return the widget for adding to the parent
