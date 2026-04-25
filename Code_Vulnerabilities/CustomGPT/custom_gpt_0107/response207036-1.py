
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create the main stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")

# Create parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
stage.add_child(parent_actor)

# Create child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 150)  # Initial size
parent_actor.add_child(child_actor)

# Custom bind constraint to maintain the width ratio
def update_child_size(actor, constraint):
    parent_size = actor.get_parent().get_width()
    new_width = parent_size / 2
    actor.set_size(new_width, actor.get_height())

# Bind constraint to the child actor
bind_constraint = Clutter.BindConstraint.new()
bind_constraint.set_target(parent_actor, Clutter.BindingType.BIND_TO_SOURCE)
bind_constraint.set_on_size_changed_callback(update_child_size)

# Add the constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Show the stage
stage.show_all()
Clutter.main()
