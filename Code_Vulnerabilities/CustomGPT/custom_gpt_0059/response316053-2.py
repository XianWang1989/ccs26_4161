
import gi
import GLib

gi.require_version('Gtk', '3.0')

# Main app loop
win = ParentWindow()
win.show_all()

# Update every second
GLib.timeout_add_seconds(1, win.clock1.update)

Gtk.main()
