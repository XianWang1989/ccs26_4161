
import gi
gi.require_version("Clutter", "1.0")
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init([])

# Create the main stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.show()

# Create the parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_background_color(Clutter.Color.from_string("blue"))
stage.add_child(parent_actor)

# Create the child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 150)  # Initial size
child_actor.set_position(100, 75)
child_actor.set_background_color(Clutter.Color.from_string("red"))
stage.add_child(child_actor)

# BindConstraint to link the child's width to half of the parent's width
width_constraint = Clutter.BindConstraint.new(parent_actor, Clutter.BindProp.WIDTH, Clutter.BindFlags.DEFAULT)
width_constraint.set_scale(0.5)  # Set scaling factor to 0.5 for half the width
child_actor.add_constraint(width_constraint)

# Show all actors
Clutter.main()
