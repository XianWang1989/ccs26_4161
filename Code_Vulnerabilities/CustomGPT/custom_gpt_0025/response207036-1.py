
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create the main stage
stage = Clutter.Stage()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")
stage.show()

# Create the parent actor
parent_actor = Clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_color(Clutter.Color.from_string("red"))
parent_actor.set_position(200, 150)
stage.add_child(parent_actor)

# Create the child actor
child_actor = Clutter.Actor()
child_actor.set_color(Clutter.Color.from_string("blue"))
child_actor.set_height(100)
parent_actor.add_child(child_actor)

# Create a BindConstraint to make child_actor's width half of parent_actor's width
bind_constraint = Clutter.BindConstraint.create(
    child_actor,                     # The actor to be constrained
    parent_actor,                   # The source actor
    Clutter.BindFlags.WIDTH,       # We want to bind the width
    0.5                             # 50% of the width
)

# Add the constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Show all actors
stage.show_all()

# Start the main loop
Clutter.main()
