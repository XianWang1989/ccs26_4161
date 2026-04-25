
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init(None)

# Create a stage
stage = Clutter.Stage()
stage.set_size(800, 600)

# Create parent actor
parent_actor = Clutter.Actor()
parent_actor.set_size(400, 200)
parent_actor.set_position(200, 200)
stage.add_child(parent_actor)

# Create child actor
child_actor = Clutter.Actor()
child_actor.set_size(200, 100)  # Initial size
child_actor.set_position(0, 0)
parent_actor.add_child(child_actor)

# BindConstraint to keep child at half the width of the parent
def update_child_size(actor, constraint):
    parent_width = parent_actor.get_width()
    new_child_width = parent_width / 2
    child_actor.set_size(new_child_width, child_actor.get_height())

# Create a BindConstraint
bind_constraint = Clutter.BindConstraint.new(parent_actor, Clutter.BindFlags.SIZE)
child_actor.add_constraint(bind_constraint)

# Connect the event to update child size
child_actor.connect("notify::width", update_child_size)

# Show all actors
stage.show()

# Main loop
Clutter.main()
