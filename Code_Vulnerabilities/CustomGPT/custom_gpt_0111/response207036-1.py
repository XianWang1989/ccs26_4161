
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init(None)

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 200)
parent_actor.set_position(200, 200)
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 100)  # Initial size
parent_actor.add_child(child_actor)

# Create the BindConstraint to maintain half the width of the parent
bind_constraint = Clutter.BindConstraint.new(parent_actor, Clutter.BindProp.WIDTH)
# Set the ratio to 0.5 (50%)
bind_constraint.set_ratio(0.5)

# Add the constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Show all actors
stage.show_all()

# Main loop
Clutter.main()
