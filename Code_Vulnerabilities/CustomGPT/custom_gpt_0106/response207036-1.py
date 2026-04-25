
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.show()

# Create parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_color(Clutter.Color.from_byte(0, 128, 0, 255))  # Green
stage.add_child(parent_actor)

# Create child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 150)  # Initial size (will be constrained)
child_actor.set_color(Clutter.Color.from_byte(255, 0, 0, 255))  # Red
parent_actor.add_child(child_actor)

# Create a BindConstraint to link child's width to half of parent's width
def update_child_size():
    parent_width = parent_actor.get_width()
    child_actor.set_size(parent_width / 2, child_actor.get_height())

# Connect the size allocation signal from the parent
parent_actor.connect('size-allocate', lambda a, allocation: update_child_size())

# Show all actors
stage.show_all()

# Start the Clutter main loop
Clutter.main()
