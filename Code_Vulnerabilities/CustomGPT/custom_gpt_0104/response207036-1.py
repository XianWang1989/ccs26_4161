
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init(None)

# Create a new stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)  # Set the size of the parent actor
parent_actor.set_position(200, 150)  # Position it in the center of the stage
parent_actor.set_color(Clutter.Color.from_string("blue"))
stage.add_child(parent_actor)

# Create the child actor
child_actor = Clutter.Actor.new()
child_actor.set_color(Clutter.Color.from_string("red"))
child_actor.set_size(200, 150)  # Initial size (we'll constrain this)
stage.add_child(child_actor)

# Function to update the child actor's size based on the parent's width
def update_child_size(actor, name):
    parent_width = actor.get_allocation().width
    child_actor.set_size(parent_width / 2, child_actor.get_allocation().height)

# Bind the child's width to half of the parent's width
bind_constraint = Clutter.BindConstraint.new(child_actor, parent_actor, Clutter.BindConstraintFlags.WIDTH)
bind_constraint.connect('notify::source', update_child_size)

# Attach the constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Show all actors
parent_actor.show()
child_actor.show()

# Start the Clutter main loop
Clutter.main()
