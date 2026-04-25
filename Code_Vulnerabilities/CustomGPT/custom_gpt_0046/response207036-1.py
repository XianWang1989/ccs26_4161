
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("Clutter BindConstraint Example")
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 200)
parent_actor.set_background_color(Clutter.Color.red())
parent_actor.set_position(200, 200)
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(100, 100)
child_actor.set_background_color(Clutter.Color.blue())
child_actor.set_position(100, 50)
parent_actor.add_child(child_actor)

# Create a BindConstraint to constrain the width of child_actor to 50% of parent_actor's width
bind_constraint = Clutter.BindConstraint.new(CuJoin(parent_actor), Clutter.BindFlags.WIDTH)
bind_constraint.set_target(parent_actor)
bind_constraint.set_property(0.5)  # Set to half the width (50%)
child_actor.add_constraint(bind_constraint)

# Show the stage
Clutter.main()
