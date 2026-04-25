
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create the main stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_background_color(Clutter.Color.from_string("blue"))
stage.add_child(parent_actor)

# Create the child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 150)  # Initial size, will be constrained
child_actor.set_position(50, 0)
child_actor.set_background_color(Clutter.Color.from_string("red"))
parent_actor.add_child(child_actor)

# Create a BindConstraint to constrain the width of the child actor
constraint = Clutter.BindConstraint.new(child_actor, Clutter.BindConstraintType.WIDTH,
                                         parent_actor, Clutter.BindConstraintType.WIDTH)

# Set the child width to half of its parent's width
constraint.set_factor(0.5)
child_actor.add_constraint(constraint)

# Show the actors
parent_actor.show()
child_actor.show()

# Start the main loop
Clutter.main()
