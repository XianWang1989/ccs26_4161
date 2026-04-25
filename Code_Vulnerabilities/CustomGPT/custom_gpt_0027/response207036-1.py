
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, Gdk

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(800, 400)
parent_actor.set_position(0, 100)
parent_actor.set_background_color(Clutter.Color.from_string("blue"))
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(0, 200)  # Initial size
child_actor.set_background_color(Clutter.Color.from_string("red"))
parent_actor.add_child(child_actor)

# Create a BindConstraint
bind_constraint = Clutter.BindConstraint.new(
    Clutter.BindConstraintSource.from_actor(parent_actor),
    Clutter.BindConstraintProperty.WIDTH,
    Clutter.BindConstraintSource.from_static_value(),
    0.5  # 50% of parent's width
)

# Apply the constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Show all actors
parent_actor.show()
child_actor.show()
Clutter.main()
