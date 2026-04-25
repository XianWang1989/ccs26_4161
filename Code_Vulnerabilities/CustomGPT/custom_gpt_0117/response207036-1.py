
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create the stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("Proportional Size Example")
stage.show()

# Create a parent actor
parent = Clutter.Actor.new()
parent.set_size(400, 300)
parent.set_position(200, 150)
parent.set_background_color(Clutter.Color.new(0, 0, 255, 255))  # Blue
stage.add_child(parent)

# Create a child actor
child = Clutter.Actor.new()
child.set_size(200, 150)  # Initial size
child.set_position(50, 50)  # Position relative to parent
child.set_background_color(Clutter.Color.new(255, 0, 0, 255))  # Red
parent.add_child(child)

# Function to update child's size based on parent's size
def update_child_size():
    parent_width = parent.get_width()
    child.set_size(parent_width / 2, child.get_height())

# Connect signals to update size on parent size change
parent.connect("size-changed", lambda actor: update_child_size())

# Show all actors
stage.show_all()

# Run the main loop
Clutter.main()
