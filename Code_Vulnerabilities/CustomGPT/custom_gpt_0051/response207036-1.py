
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create main stage
stage = Clutter.Stage()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_color(Clutter.Color.from_string("blue"))
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor()
child_actor.set_color(Clutter.Color.from_string("red"))
parent_actor.add_child(child_actor)

# Create the BindConstraint to bind the child's width
bind_constraint = Clutter.BindConstraint.new(child_actor, Clutter.BindParam.WIDTH, parent_actor, Clutter.BindParam.WIDTH)
bind_constraint.set_scale(0.5)  # Set to half the width of the parent

# Apply the constraint
child_actor.add_constraint(bind_constraint)

# Show the actors
parent_actor.show()
child_actor.show()

# Start the main loop
Clutter.main()
