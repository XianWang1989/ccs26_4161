
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init(None)

# Create the parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 200)  # Set parent size

# Create the child actor
child_actor = Clutter.Actor.new()
child_actor.set_color(Clutter.Color.from_string("blue"))
child_actor.set_size(200, 200)  # Initial size

# Add actors to the stage
stage = Clutter.Stage.new()
stage.add_child(parent_actor)
stage.add_child(child_actor)

# Create a BindConstraint to set child's width to half of parent's width
bind_constraint = Clutter.BindConstraint.new(Clutter.BindFlags.WIDTH, parent_actor, Clutter.BindFlags.WIDTH)
bind_constraint.set_scale(0.5)  # Scale to 50%

# Add the constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Show the stage
stage.show()

# Start the Clutter main loop
Clutter.main()
