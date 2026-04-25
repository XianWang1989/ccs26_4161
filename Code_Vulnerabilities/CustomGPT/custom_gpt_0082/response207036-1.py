
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create the stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("Bind Constraint Example")
stage.show()

# Create parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(200, 200)
parent_actor.set_background_color(Clutter.Color.from_string("blue"))
stage.set_child(parent_actor)

# Create child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(100, 100)
child_actor.set_background_color(Clutter.Color.from_string("red"))
parent_actor.add_child(child_actor)

# Create a BindConstraint to link the child's width to half of the parent's width
def update_child_size():
    parent_width = parent_actor.get_width()
    new_width = parent_width / 2
    child_actor.set_size(new_width, child_actor.get_height())

# Connect the update function to the parent size change
parent_actor.connect("size-changed", lambda actor, event: update_child_size())

# Show actors
parent_actor.show()
child_actor.show()

# Main loop
Clutter.main()
