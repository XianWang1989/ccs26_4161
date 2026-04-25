
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init(None)

# Create a stage and set its size
stage = Clutter.Stage.new()
stage.set_size(600, 400)
stage.show()

# Create the parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(300, 200)
parent_actor.set_position(50, 100)
stage.add_child(parent_actor)

# Create the child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(150, 100)  # Initial size
child_actor.set_position(0, 0)
parent_actor.add_child(child_actor)

# Create a custom BindConstraint to maintain half width
def bind_half_width(source, target):
    # Get the parent's width and set child's width to half
    parent_width = source.get_width()
    new_width = parent_width / 2
    target.set_size(new_width, target.get_height())

# Create BindConstraint
constraint = Clutter.BindConstraint.new(parent_actor, "width")
constraint.set_target_value(0.5)  # Set target proportion to 50%

# Add the constraint to the child actor
child_actor.add_constraint(constraint)

# Show the actors
parent_actor.show()
child_actor.show()

# Main loop
Clutter.main()
