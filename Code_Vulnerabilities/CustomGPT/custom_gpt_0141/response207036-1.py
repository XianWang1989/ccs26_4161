
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, Gio

# Create a new stage
Clutter.init([])
stage = Clutter.Stage()
stage.set_title("BindConstraint Example")
stage.set_size(800, 600)
stage.show()

# Create a parent actor
parent = Clutter.Actor()
parent.set_size(400, 300)
parent.set_position(200, 150)
parent.set_background_color(Clutter.Color.from_string("blue"))
stage.add_child(parent)

# Create a child actor
child = Clutter.Actor()
child.set_size(200, 150)  # Initial size
child.set_position(10, 10)
child.set_background_color(Clutter.Color.from_string("red"))
parent.add_child(child)

# Function to update the child's width based on the parent's width
def update_child_size(actor, param, data):
    parent_width = actor.get_width()  # Get the parent's width
    new_width = int(parent_width * 0.5)  # Set the child's width to 50% of parent's width
    child.set_size(new_width, child.get_height())  # Update child's size

# Create a bind constraint for the parent's width
bind_constraint = Clutter.BindConstraint.new(parent, Clutter.BindingFlags.WIDTH)
bind_constraint.set_flags(Clutter.BindingFlags.WIDTH)
bind_constraint.connect("notify::width", update_child_size)  # Connect to notify signal
child.add_constraint(bind_constraint)  # Add the constraint to the child

# Start the main loop
Clutter.main()
