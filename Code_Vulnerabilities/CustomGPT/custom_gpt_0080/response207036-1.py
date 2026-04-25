
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_background_color(Clutter.Color.from_string("blue"))
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(100, 300)  # Initial size
child_actor.set_position(0, 0)
child_actor.set_background_color(Clutter.Color.from_string("red"))
parent_actor.add_child(child_actor)

# Create a BindConstraint to make child 50% of parent's width
constraint = Clutter.BindConstraint.new()
constraint.set_target(parent_actor)
constraint.set_target_property("width")
constraint.set_source_property("width")
constraint.set_scale(0.5)  # Scale to 50%
child_actor.add_constraint(constraint)

# Show the stage
stage.show()
Clutter.main()
