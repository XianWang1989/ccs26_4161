
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, Gio

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 400)
parent_actor.set_position(200, 100)
parent_actor.set_background_color(Clutter.Color.from_string("grey"))
stage.add_child(parent_actor)

# Create the child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 200)  # Initial size
child_actor.set_position(100, 100)
child_actor.set_background_color(Clutter.Color.from_string("blue"))
parent_actor.add_child(child_actor)

# Create a bind constraint for the child actor's width to be half of parent's width
bind_constraint = Clutter.BindConstraint.new(child_actor, 
    Clutter.BindFlags.WIDTH, parent_actor, 
    Clutter.BindFlags.WIDTH)

# Adjust the scale factor to 0.5 (half)
bind_constraint.set_scale_factor(0.5)

# Add the constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Show the actors
Clutter.main()
