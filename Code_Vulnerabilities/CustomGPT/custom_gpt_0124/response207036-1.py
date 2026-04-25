
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create a main stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_background_color(Clutter.Color.from_string("blue"))
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(100, 100)
child_actor.set_position(0, 0)
child_actor.set_background_color(Clutter.Color.from_string("red"))
parent_actor.add_child(child_actor)

# Create a BindConstraint to bind the child's width to half of the parent's width
bind_constraint = Clutter.BindConstraint.new(Clutter.BindDimension.WIDTH, parent_actor, Clutter.BindDimension.WIDTH)
bind_constraint.set_factor(0.5)  # Set the factor to 0.5 for half width
child_actor.add_constraint(bind_constraint)

# Main loop to keep the stage open
Clutter.main()
