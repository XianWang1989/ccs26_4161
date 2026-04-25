
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create a stage (the main window)
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 150)  # Initial size (will be overridden)
child_actor.set_position(0, 0)
parent_actor.add_child(child_actor)

# Create a BindConstraint to link child's width to half of parent's width
constraint = Clutter.BindConstraint.new(
    Clutter.BindFlags.SIZE_X,
    parent_actor,
    Clutter.BindFlags.SIZE_X,
    0.5  # This sets the child actor's width to 50% of the parent's width
)

# Apply the constraint to the child actor
child_actor.add_constraint(constraint)

# Show the actors
parent_actor.show()
child_actor.show()

# Start the main loop
Clutter.main()
