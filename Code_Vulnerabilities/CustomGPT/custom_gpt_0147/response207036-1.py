
import sys
from gi.repository import Clutter, Cogl

# Initialize Clutter
Clutter.init(sys.argv)

# Create a stage
stage = Clutter.Stage()
stage.set_size(800, 600)
stage.set_title("Clutter BindConstraint Example")
stage.show()

# Create a parent actor (rectangle)
parent_actor = Clutter.Rectangle()
parent_actor.set_size(200, 100)
parent_actor.set_color(Clutter.Color.from_string("blue"))
parent_actor.set_position(300, 250)
stage.add_child(parent_actor)

# Create a child actor (rectangle)
child_actor = Clutter.Rectangle()
child_actor.set_color(Clutter.Color.from_string("red"))
child_actor.set_size(100, 50)
child_actor.set_position(310, 255)
stage.add_child(child_actor)

# Create a bind constraint
bind_constraint = Clutter.BindConstraint()
bind_constraint.set_source(parent_actor)

# Set width to 50% of the parent's width
bind_constraint.set_property("width", 0.5)

# Add the bind constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Main loop
Clutter.main()
