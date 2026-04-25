
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("Bind Constraint Example")

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 400)
parent_actor.set_rect(200, 100, 400, 400)
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 200)
child_actor.set_background_color(Clutter.Color.from_string("red"))
parent_actor.add_child(child_actor)

# Define a BindConstraint to keep the child's width at 50% of parent's width
def bind_constraint_callback(constraint, actor, source):
    parent_width = source.get_width()
    new_width = parent_width / 2
    actor.set_size(new_width, actor.get_height())

constraint = Clutter.BindConstraint.new(parent_actor)
constraint.set_target(parent_actor)  # Set the parent as the source
constraint.connect("notify::target", bind_constraint_callback)

# Apply the bind constraint
child_actor.add_constraint(constraint)

# Show the stage
stage.show()
Clutter.main()
