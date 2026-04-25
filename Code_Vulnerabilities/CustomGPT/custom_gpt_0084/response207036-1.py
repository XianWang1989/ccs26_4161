
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init(None)

# Create a stage (parent actor)
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)  # Set size of parent actor
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(100, 100)  # Initial size of child actor
parent_actor.add_child(child_actor)

# Create a BindConstraint to enforce the width constraint
constraint = Clutter.BindConstraint.new(child_actor, Clutter.BindConstraintType.WIDTH, parent_actor, Clutter.BindConstraintType.WIDTH)
constraint.set_factor(0.5)  # Set the factor to 0.5 for half the width
child_actor.add_constraint(constraint)

# Show the actors
parent_actor.show()
child_actor.show()

# Main loop
Clutter.main()
