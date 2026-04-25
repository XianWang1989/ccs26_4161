
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init(None)

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 200)  # Set the size of the parent actor
parent_actor.set_name("Parent Actor")

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(100, 200)  # Initial size
child_actor.set_name("Child Actor")

# Add both actors to the stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.add_child(parent_actor)
parent_actor.add_child(child_actor)

# Create a size binding to keep the child's width half of the parent's width
def update_child_size(actor, constraint):
    parent_width = actor.get_width()
    child_width = parent_width / 2
    child_actor.set_size(child_width, child_actor.get_height())

# Create a BindConstraint to link the width of the child to the parent
bind_constraint = Clutter.BindConstraint.new(parent_actor, 
                                              Clutter.BindFlags.WIDTH)
bind_constraint.set_target_value(0.5)  # Target width relative to parent

# Apply the constraint
child_actor.add_constraint(bind_constraint)

# Connect the constraints to update on size changes
parent_actor.connect("size-changed", update_child_size)

# Show the stage
stage.show_all()
Clutter.main()
