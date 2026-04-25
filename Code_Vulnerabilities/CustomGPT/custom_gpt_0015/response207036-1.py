
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init(None)

# Create the stage (main window)
stage = Clutter.Stage.new()
stage.set_title("BindConstraint Example")
stage.set_size(400, 400)
stage.set_color(Clutter.Color.from_string("white"))

# Create parent actor
parent = Clutter.Actor.new()
parent.set_size(200, 200)
parent.set_style("border: 2px solid black;")
stage.add_child(parent)

# Create child actor
child = Clutter.Actor.new()
child.set_size(100, 100)  # Initial size
child.set_style("background-color: blue;")
parent.add_child(child)

# Bind the child width to be half of the parent's width
def update_child_size():
    parent_width = parent.get_width()
    child.set_width(parent_width // 2)

# Connect to signal for resizing
parent.connect("size-changed", lambda actor: update_child_size())

# Initial size adjustment
update_child_size()

# Show the stage
stage.show_all()
Clutter.main()
