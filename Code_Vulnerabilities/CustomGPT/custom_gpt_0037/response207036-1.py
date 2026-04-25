
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create the stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)

# Create the parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_background_color(Clutter.Color.from_string("red"))
stage.add_child(parent_actor)

# Create the child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 150)  # Starting size
child_actor.set_position(150, 100)
child_actor.set_background_color(Clutter.Color.from_string("blue"))
stage.add_child(child_actor)

# Create a BindConstraint to keep the child at 50% of the parent's width
constraint = Clutter.BindConstraint.new(parent_actor, Clutter.BindDimension.WIDTH)
child_actor.add_constraint(constraint)

# Function to update the child's size based on parent's size
def update_child_size():
    parent_width = parent_actor.get_width()
    new_child_width = parent_width / 2
    child_actor.set_size(new_child_width, child_actor.get_height())

# Connect the signal to update size when the parent resizes
parent_actor.connect("notify::width", update_child_size)

# Show the stage
stage.show()

# Run the main loop
Clutter.main()
