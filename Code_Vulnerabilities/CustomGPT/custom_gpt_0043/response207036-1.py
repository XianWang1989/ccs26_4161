
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("Clutter BindConstraint Example")
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_color(Clutter.Color.from_string("red"))
parent_actor.set_position(200, 150)
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 150)
child_actor.set_color(Clutter.Color.from_string("blue"))
child_actor.set_position(0, 0)  # Initial position
parent_actor.add_child(child_actor)

# Create a BindConstraint to bind the width of the child actor to half of the parent's width
def bind_half_width(source_actor, target_actor):
    # Calculate the target width as half of the source's width
    source_width = source_actor.get_width()
    target_width = int(source_width * 0.5)  # Half the width

    # Set the new width
    target_actor.set_width(target_width)

# Create a BindConstraint with a callback function
constraint = Clutter.BindConstraint.new(parent_actor, Clutter.BindFlags.SIZE)
constraint.set_source_actor(parent_actor)

# Connect the width change of the parent actor to update the child's width
parent_actor.connect("notify::width", lambda actor: bind_half_width(actor, child_actor))

# Initial binding setup
bind_half_width(parent_actor, child_actor)

# Show the stage
Clutter.main()
