
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("Clutter Example")

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 200)
parent_actor.set_position(200, 200)
parent_actor.set_background_color(Clutter.Color.from_string("blue"))  # blue background
stage.add_child(parent_actor)

# Create a child actor that we will bind to the parent
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 100)  # Initial size
child_actor.set_position(100, 50)
child_actor.set_background_color(Clutter.Color.from_string("red"))  # red background
stage.add_child(child_actor)

# Create a bind constraint to maintain the child's width at half of the parent's width
constraint = Clutter.BindConstraint.new(child_actor, Clutter.BindProp.WIDTH, parent_actor, Clutter.BindProp.WIDTH)
constraint.set_scale(0.5)  # Set the scale to 0.5 to maintain half the width
child_actor.add_constraint(constraint)

# Show the stage
stage.show_all()
Clutter.main()
