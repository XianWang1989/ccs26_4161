
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init(None)

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")

# Create a parent actor (e.g., a rectangle)
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 200)
parent_actor.set_background_color(Clutter.Color.from_string("blue"))
parent_actor.set_position(200, 200)  # Center on stage
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 100)
child_actor.set_background_color(Clutter.Color.from_string("red"))
child_actor.set_position(50, 50)  # Offset in parent
parent_actor.add_child(child_actor)

# Create a binding constraint for width
def update_child_size():
    parent_width = parent_actor.get_width()
    child_actor.set_width(parent_width // 2)

# Connect signals to update child width when the parent is resized
parent_actor.connect('notify::width', lambda actor: update_child_size())

# Show actors
stage.show_all()

# Start the main loop
Clutter.Main.run()
