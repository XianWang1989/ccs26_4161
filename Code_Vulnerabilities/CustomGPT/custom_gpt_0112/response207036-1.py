
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init(None)

# Create the main stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_color(Clutter.Color.from_string("blue"))
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_height(100)
child_actor.set_color(Clutter.Color.from_string("red"))
parent_actor.add_child(child_actor)

# Create a BindConstraint to bind the width of the child to 50% of the parent
bind_constraint = Clutter.BindConstraint.new(
    Clutter.BindConstraintTarget.WIDTH,        # Binding to the width
    0.5,                                        # 50% of the target
    0,                                          # Relative to the parent
    None                                        # No additional actor, just the parent
)

# Add the constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Show all actors
parent_actor.show()
child_actor.show()
Clutter.main()
