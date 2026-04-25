
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(400, 300)
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(200, 200)
parent_actor.set_color(Clutter.Color.new(255, 0, 0, 255))  # Red
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(100, 100)  # This will be modified by the constraint
child_actor.set_color(Clutter.Color.new(0, 0, 255, 255))  # Blue
parent_actor.add_child(child_actor)

# Create a bind constraint to make the child actor's width half of the parent's width
def update_child_size(child, parent):
    parent_width = parent.get_width()
    # Set child width to half of parent's width
    child.set_size(parent_width // 2, child.get_height())

# Connect the update function to the parent's "size-changed" signal
parent_actor.connect("size-changed", update_child_size, child_actor)

# Initial size update
update_child_size(child_actor, parent_actor)

# Show the stage
Clutter.main()
