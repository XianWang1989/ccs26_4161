
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create the main stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 100)
parent_actor.set_position(200, 250)
parent_actor.set_background_color(Clutter.Color.new(0, 255, 0, 255))  # Green
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 50)  # Initial size, will be constrained
child_actor.set_position(0, 25)  # Center vertically
child_actor.set_background_color(Clutter.Color.new(255, 0, 0, 255))  # Red
parent_actor.add_child(child_actor)

# Create a bind constraint to set child width to half of parent's width
def update_child_width():
    parent_width = parent_actor.get_width()
    child_actor.set_size(parent_width / 2, child_actor.get_height())

# Add a signal to call `update_child_width` whenever the parent size changes
parent_actor.connect('size-changed', lambda actor, *args: update_child_width())

# Initial call to set child size
update_child_width()

# Show the stage
Clutter.main()
