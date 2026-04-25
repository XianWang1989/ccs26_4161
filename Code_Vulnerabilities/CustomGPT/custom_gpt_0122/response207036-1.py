
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init(None)

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.show()

# Create parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_background_color(Clutter.Color(0, 255, 0, 255))  # Green
stage.add_child(parent_actor)

# Create child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 150)
child_actor.set_background_color(Clutter.Color(255, 0, 0, 255))  # Red
parent_actor.add_child(child_actor)

# Function to update child width
def update_child_size(*args):
    parent_width = parent_actor.get_width()
    new_width = parent_width // 2  # 1/2 the parent's width
    child_actor.set_width(new_width)

# Bind the size update to parent's size-changed signal
parent_actor.connect("size-changed", update_child_size)

# Initial size update
update_child_size()

# Show all actors
Clutter.main()
