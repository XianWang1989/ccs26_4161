
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create a stage and show it
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")
stage.show()

# Create the parent actor
parent = Clutter.Actor.new()
parent.set_size(400, 300)
parent.set_position(200, 150)
parent.set_color(Clutter.Color.from_string("blue"))
stage.add_child(parent)

# Create the child actor
child = Clutter.Actor.new()
child.set_size(200, 150)  # Initially set size
child.set_position(0, 0)
child.set_color(Clutter.Color.from_string("red"))
parent.add_child(child)

# Create a BindConstraint for the child to be half the width of the parent
constraint = Clutter.BindConstraint.new(child,
                                         parent,
                                         Clutter.BindFlags.WIDTH,
                                         Clutter.BindStrength.NORMAL)
constraint.set_coefficients(0.5, 0)  # Set to half the width
child.add_constraint(constraint)

# Start the main loop
Clutter.main()
