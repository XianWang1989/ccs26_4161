
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, Gdk

# Initialize Clutter
Clutter.init([])

# Create the main stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.show()

# Create parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_color(Clutter.Color.new(255, 0, 0, 255))  # Red
stage.add_child(parent_actor)

# Create child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(100, 100)  # Initial size, will be constrained
child_actor.set_position(50, 50)
child_actor.set_color(Clutter.Color.new(0, 255, 0, 255))  # Green
parent_actor.add_child(child_actor)

# Create a binding to set the child's width to half of the parent's width
Clutter.BindConstraint.new(child_actor, "width", parent_actor, "width", 0.5)

# Show all actors
stage.show_all()

# Start the main loop
Clutter.main()
