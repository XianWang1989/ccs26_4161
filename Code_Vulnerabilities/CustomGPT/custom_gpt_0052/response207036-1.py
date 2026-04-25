
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init([])

# Create a main stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")

# Create the parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_background_color(Clutter.Color.from_string("lightblue"))
stage.add_child(parent_actor)

# Create the child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 150)  # Initial size (will be constrained)
child_actor.set_background_color(Clutter.Color.from_string("pink"))
parent_actor.add_child(child_actor)

# Create a BindConstraint to keep the child actor's width at half of the parent's width
bind_constraint = Clutter.BindConstraint.new(parent_actor, Clutter.BindDimension.WIDTH)
bind_constraint.set_factor(0.5)  # Set to 50% of the parent's width

# Add the constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Show the stage
stage.show()

# Start the main loop
Clutter.main()
