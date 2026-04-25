
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage.new()
stage.set_title("BindConstraint Example")
stage.set_size(800, 600)
stage.set_color(Clutter.Color.from_string("white"))
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_color(Clutter.Color.from_string("blue"))
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_color(Clutter.Color.from_string("red"))
parent_actor.add_child(child_actor)

# Function to update child's width based on parent's width
def update_child_size():
    parent_width = parent_actor.get_width()
    child_actor.set_width(parent_width // 2)  # Set child's width to half of parent's width

# Call the function once to set initial size
update_child_size()

# Create a BindConstraint to link the child actor's width to the parent's width
def on_parent_size_changed(actor, param, user_data):
    update_child_size()

# Connect the size-changed signal of the parent actor
parent_actor.connect("notify::width", on_parent_size_changed)

# Show all the actors
parent_actor.show()
child_actor.show()

# Main loop
Clutter.main()
