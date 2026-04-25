
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init(None)

# Create the main stage
stage = Clutter.Stage()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")

# Create the parent actor
parent_actor = Clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_background_color(Clutter.Color.from_string("blue"))
stage.add_child(parent_actor)

# Create the child actor
child_actor = Clutter.Actor()
child_actor.set_size(200, 150)  # Initial size
child_actor.set_position(50, 50)
child_actor.set_background_color(Clutter.Color.from_string("red"))
parent_actor.add_child(child_actor)

# Function to update child's width based on parent's width
def update_child_size(parent, child):
    # Calculate new width as half of parent's width
    new_width = parent.get_width() / 2
    child.set_width(new_width)

# BindConstraint sets the width of the child to 1/2 of the parent's width
bind_constraint = Clutter.BindConstraint.new(parent_actor, 
                                               Clutter.BindSet.WIDTH, 
                                               Clutter.BindSource.WIDTH, 
                                               0.5)  # Proportion 0.5 for half
child_actor.add_constraint(bind_constraint)

# Connect the signal to update the child's size whenever the parent's size changes
parent_actor.connect("size-changed", update_child_size, child_actor)

# Show everything on the stage
stage.show_all()

# Start the main loop
Clutter.Main()
