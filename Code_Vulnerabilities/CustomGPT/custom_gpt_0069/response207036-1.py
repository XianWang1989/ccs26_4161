
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")

# Create parent actor
parent_actor = Clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_background_color(Clutter.Color.from_string("blue"))
stage.add_child(parent_actor)

# Create child actor
child_actor = Clutter.Actor()
child_actor.set_size(200, 150)  # Initial size
child_actor.set_position(50, 50)
child_actor.set_background_color(Clutter.Color.from_string("red"))
parent_actor.add_child(child_actor)

# Create a bind constraint
constraint = Clutter.BindConstraint.new(child_actor, Clutter.BindFlags.WIDTH, parent_actor, Clutter.BindFlags.WIDTH)

# Set the proportion (1/2 of the parent's width)
constraint.set_scale(0.5)

# Add the constraint to the child actor
child_actor.add_constraint(constraint)

# Show the stage
stage.show()

# Start the main loop
Clutter.main()
