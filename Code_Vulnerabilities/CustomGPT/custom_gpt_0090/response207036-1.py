
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init(None)

# Create a stage
stage = Clutter.Stage()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")
stage.show()

# Create parent actor
parent_actor = Clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_background_color(Clutter.Color.from_string("blue"))
stage.add_child(parent_actor)

# Create child actor
child_actor = Clutter.Actor()
child_actor.set_size(200, 150)  # Initial size
child_actor.set_position(0, 0)
child_actor.set_background_color(Clutter.Color.from_string("red"))
parent_actor.add_child(child_actor)

# Create a BindConstraint to bind child's width to half of parent's width
bind_constraint = Clutter.BindConstraint.new(
    child_actor, 
    Clutter.BindDimension.WIDTH, 
    parent_actor, 
    Clutter.BindDimension.WIDTH, 
    0.5  # Set ratio to 1/2
)
child_actor.add_constraint(bind_constraint)

# Show actors
parent_actor.show()
child_actor.show()

# Start the Clutter main loop
Clutter.main()
