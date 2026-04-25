
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init([])

# Create a stage and set its properties
stage = Clutter.Stage()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor()
parent_actor.set_size(400, 300)  # Parent dimensions
parent_actor.set_position(200, 150)
parent_actor.set_background_color(Clutter.Color.from_string("lightblue"))
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor()
child_actor.set_size(200, 150)  # Initial size
child_actor.set_position(50, 50)
child_actor.set_background_color(Clutter.Color.from_string("salmon"))
parent_actor.add_child(child_actor)

# Create a BindConstraint to bind the child's width to half of the parent's width
def update_child_size(actor):
    parent_width = parent_actor.get_width()
    # Set child's width to half of parent's width
    child_actor.set_size(parent_width / 2, child_actor.get_height())

# Connect the 'allocation-changed' signal to update the child size when the parent changes size
parent_actor.connect("allocation-changed", update_child_size)

# Show the stage and all actors
stage.show_all()

# Start the main loop
Clutter.main()
