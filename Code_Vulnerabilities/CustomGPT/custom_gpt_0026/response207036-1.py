
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init(None)

# Create a stage and set its size
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")

# Create the parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 200)
parent_actor.set_position(200, 200)
parent_actor.set_color(Clutter.Color.new(0, 0, 255, 255))  # Blue
stage.add_child(parent_actor)

# Create the child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 100)
child_actor.set_position(0, 0)
child_actor.set_color(Clutter.Color.new(255, 0, 0, 255))  # Red
parent_actor.add_child(child_actor)

# Create a BindConstraint to keep the child's width at half of the parent's width
bind_constraint = Clutter.BindConstraint.new(parent_actor, Clutter.BindFlags.WIDTH)
bind_constraint.set_factor(0.5)  # Set the factor to 1/2 (50%)
child_actor.add_constraint(bind_constraint)

# Show the stage
stage.show_all()
Clutter.main()
