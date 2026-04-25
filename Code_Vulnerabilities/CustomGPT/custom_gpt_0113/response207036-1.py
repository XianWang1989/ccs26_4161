
import gi
gi.require_version('Clutter', '1.0')
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
parent_actor.set_background_color(Clutter.Color.from_rgba(0, 0, 255, 255))  # Blue
stage.add_child(parent_actor)

# Create the child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 150)  # Initial size (will be constrained)
child_actor.set_position(20, 20)
child_actor.set_background_color(Clutter.Color.from_rgba(255, 0, 0, 255))  # Red
parent_actor.add_child(child_actor)

# Create a BindConstraint to set the child's width to half of the parent's width
width_constraint = Clutter.BindConstraint.new(parent_actor, Clutter.BindDimension.WIDTH, 0.5)
child_actor.add_constraint(width_constraint)

# Show all actors
stage.show_all()

# Start the main loop
Clutter.main()
