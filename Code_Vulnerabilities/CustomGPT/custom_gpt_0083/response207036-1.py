
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init(None)

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 150)  # Initial size
child_actor.set_position(50, 50)
parent_actor.add_child(child_actor)

# Create a BindConstraint to keep child_actor's width at half of parent_actor's width
bind_constraint = Clutter.BindConstraint.new(Clutter.BindConstraintType.WIDTH, parent_actor, Clutter.BindConstraintType.WIDTH)
bind_constraint.set_scale(0.5)  # Scale to 50%
child_actor.add_constraint(bind_constraint)

# Main loop
Clutter.main()
