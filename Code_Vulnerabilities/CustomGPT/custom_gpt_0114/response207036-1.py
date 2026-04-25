
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create the main stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")
stage.show()

# Create a parent actor
parent = Clutter.Actor.new()
parent.set_size(400, 200)
parent.set_position(200, 200)
stage.add_child(parent)

# Create a child actor
child = Clutter.Actor.new()
child.set_size(200, 100)  # Initial size but will be constrained
child.set_position(0, 0)
parent.add_child(child)

# Create a BindConstraint to constrain the child's width to half of the parent's width
constraint = Clutter.BindConstraint.new(Clutter.Actor.Prop.WIDTH, parent, Clutter.Actor.Prop.WIDTH, 0.5)
child.add_constraint(constraint)

# Show all actors
stage.show_all()

# Start the main loop
Clutter.main()
