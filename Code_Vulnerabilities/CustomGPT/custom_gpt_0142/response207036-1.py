
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
parent_actor.set_position(200, 150)
parent_actor.set_background_color(Clutter.Color.from_string("red"))
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 100)
child_actor.set_background_color(Clutter.Color.from_string("blue"))
parent_actor.add_child(child_actor)

# Create a bind constraint that keeps the child's width half of the parent's width
def update_child_size(child, parent):
    parent_width = parent.get_width()
    child.set_size(parent_width / 2, child.get_height())

# Apply the bind constraint
bind_constraint = Clutter.BindConstraint.new(child_actor, parent_actor, Clutter.BindFlags.WIDTH)
child_actor.add_constraint(bind_constraint)

# Connect signal to update child size on parent size changes
parent_actor.connect("size-changed", update_child_size, child_actor)

# Show all actors
stage.show_all()

# Start the Clutter main loop
Clutter.main()
