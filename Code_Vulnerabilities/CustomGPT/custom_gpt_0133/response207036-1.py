
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init(None)

# Create a stage
stage = Clutter.Stage() 
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")
stage.show()

# Create a parent actor
parent = Clutter.Actor()
parent.set_size(400, 300)
parent.set_position(200, 150)
parent.set_color(Clutter.Color.from_string("red"))  # Set a color for visibility
stage.add_child(parent)

# Create a child actor
child = Clutter.Actor()
child.set_size(200, 150)
child.set_position(50, 50)  # Set position relative to parent
child.set_color(Clutter.Color.from_string("blue"))  # Set a color for visibility
parent.add_child(child)

# Create a bind constraint that sets the child's width to half of the parent's width
bind_constraint = Clutter.BindConstraint.new(
    child,
    Clutter.BindConstraintProperty.WIDTH,
    parent,
    Clutter.BindConstraintProperty.WIDTH,
    0.5  # Proportional factor to set children width as half of its parent's width
)

# Add the constraint to the child actor
child.add_constraint(bind_constraint)

# Show the stage
Clutter.main()
