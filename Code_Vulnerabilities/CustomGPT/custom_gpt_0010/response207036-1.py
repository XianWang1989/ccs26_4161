
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, Cogl

# Initialize Clutter
Clutter.init([])

# Create an Actor (Parent)
parent = Clutter.Actor()
parent.set_size(400, 300)  # Set size of parent
parent.set_color(Clutter.Color.from_string("blue"))

# Create a Child Actor
child = Clutter.Actor()
child.set_color(Clutter.Color.from_string("red"))

# Bind the child's width to half of the parent's width
bind_constraint = Clutter.BindConstraint.new(child, Clutter.BindDimension.WIDTH, parent, Clutter.BindDimension.WIDTH)
bind_constraint.set_scale(0.5)  # Scale it to half
child.add_constraint(bind_constraint)

# Add actors to the stage
stage = Clutter.Stage()
stage.set_size(800, 600)
stage.add_child(parent)
stage.add_child(child)

# Position the child actor
child.set_position(50, 100)  # Adjust as necessary

# Show the stage
stage.show_all()
Clutter.main()
