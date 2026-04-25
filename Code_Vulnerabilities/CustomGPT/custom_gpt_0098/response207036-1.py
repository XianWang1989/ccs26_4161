
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 400)
parent_actor.set_position(200, 100)
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 200)  # Initial size
parent_actor.add_child(child_actor)

# Bind the child's width to half of the parent's width
def update_child_size(source_actor, *args):
    parent_width = source_actor.get_width()
    child_actor.set_size(parent_width // 2, child_actor.get_height())

# Connect signal to update child size when parent's size changes
parent_actor.connect("size-changed", update_child_size)

# Show the actors
parent_actor.show()
child_actor.show()

# Start the main loop
Clutter.main()
