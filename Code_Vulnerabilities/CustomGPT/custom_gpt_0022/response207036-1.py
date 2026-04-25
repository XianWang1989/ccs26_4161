
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_background_color(Clutter.Color.from_string("blue"))
parent_actor.set_position(200, 150)
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 150)  # Initial size
child_actor.set_background_color(Clutter.Color.from_string("red"))
child_actor.set_position(100, 75)
parent_actor.add_child(child_actor)

# Create a bind constraint to keep the child's width at 50% of the parent's width
def resize_child(source_actor, target_actor):
    parent_width = source_actor.get_width()
    new_width = int(parent_width * 0.5)  # 50% of parent's width
    child_actor.set_size(new_width, child_actor.get_height())

# Connect the resizing function to the parent's width change
parent_actor.connect("notify::width", resize_child)

# Show the actors
parent_actor.show()
child_actor.show()

# Start the main loop
Clutter.main()
