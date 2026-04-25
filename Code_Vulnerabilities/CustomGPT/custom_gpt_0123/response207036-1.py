
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init(None)

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.show()

# Create parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_background_color(Clutter.Color.from_string("blue"))
stage.add_child(parent_actor)

# Create child actor
child_actor = Clutter.Actor.new()
child_actor.set_background_color(Clutter.Color.from_string("red"))

# BindConstraint to set child's width to half of parent's width
bind_constraint = Clutter.BindConstraint.new()
bind_constraint.set_source(parent_actor, Clutter.ActorProperty.WIDTH)
bind_constraint.set_target(child_actor, Clutter.ActorProperty.WIDTH)
bind_constraint.set_ratio(0.5)  # Set ratio to 0.5 for half the width

# Add the constraint
child_actor.add_constraint(bind_constraint)

# Set child's height and add it to the parent
child_actor.set_size(200, 150)  # Set height as desired
parent_actor.add_child(child_actor)

# Show everything
stage.show_all()

# Start the main loop
Clutter.main()
