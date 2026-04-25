
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create a new stage
stage = Clutter.Stage.new()
stage.set_size(400, 400)
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 400)
parent_actor.set_background_color(Clutter.Color.new(255, 0, 0, 255))  # Red
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_background_color(Clutter.Color.new(0, 0, 255, 255))  # Blue
parent_actor.add_child(child_actor)

# Function to update the size of the child actor
def update_size():
    parent_width = parent_actor.get_width()
    child_actor.set_size(parent_width // 2, parent_actor.get_height())

# Connect the "notify::width" signal to update the size of the child actor
parent_actor.connect("notify::width", lambda actor, param: update_size())
parent_actor.connect("notify::height", lambda actor, param: update_size())

update_size()  # Initial size update

# Show the actors
stage.show_all()
Clutter.main()
