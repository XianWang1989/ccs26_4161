
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_color(Clutter.Color.from_string("blue"))
parent_actor.set_position(200, 150)
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor()
child_actor.set_color(Clutter.Color.from_string("red"))
parent_actor.add_child(child_actor)

# Function to bind child's width to half of parent's width
def update_child_size():
    parent_width = parent_actor.get_width()
    child_actor.set_size(parent_width / 2, child_actor.get_height())

# Call the update function initially
update_child_size()

# Connect the size-changed signal of the parent actor to the update function
parent_actor.connect("notify::width", update_child_size)
parent_actor.connect("notify::height", update_child_size)

# Show the child actor
child_actor.show()

# Enter the main loop
Clutter.main()
