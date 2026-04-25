
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 200)  # Set parent size
parent_actor.set_position(200, 200)  # Center it
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 100)  # Set initial size
child_actor.set_position(0, 0)   # Position it within the parent
parent_actor.add_child(child_actor)

# Create a BindConstraint to constrain the width of the child to half of the parent's width
from gi.repository import Clutter

def on_parent_size_changed(actor, param):
    parent_width = actor.get_width()
    child_width = parent_width / 2
    child_actor.set_size(child_width, child_actor.get_height())

# Connect the signal to update the child actor's size
parent_actor.connect("notify::width", on_parent_size_changed)
parent_actor.connect("notify::height", on_parent_size_changed)

# Show all actors
parent_actor.show()
child_actor.show()

# Start the main loop
Clutter.main()
