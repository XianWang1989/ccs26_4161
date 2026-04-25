
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, Gio

# Initialize Clutter
Clutter.init([])

# Create a stage and set its size
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 150)  # Initial size
parent_actor.add_child(child_actor)

# Create a custom bind constraint to set child's width to half of parent's width
def half_width_constraint(child, parent):
    parent_width = parent.get_width()
    child.set_width(parent_width // 2)

# Connect the bind constraint to resize the child whenever the parent resizes
parent_actor.connect("notify::width", lambda actor: half_width_constraint(child_actor, actor))

# Show the actors
stage.show_all()

# Run the Clutter main loop
Clutter.threads_init()
Clutter.main()
