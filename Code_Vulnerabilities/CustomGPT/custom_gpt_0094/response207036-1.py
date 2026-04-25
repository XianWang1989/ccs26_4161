
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")
stage.show()

# Create parent actor
parent = Clutter.Actor()
parent.set_size(400, 300)
parent.set_position(200, 150)
stage.add_child(parent)

# Create child actor
child = Clutter.Actor()
child.set_size(200, 150)
child.set_position(0, 0)
parent.add_child(child)

# Create BindConstraint to tie child's width to half of parent's width
constraint = Clutter.BindConstraint.create(GObject.TYPE_FLOAT, 
                                            Clutter.BindConstraint.BindType.WIDTH, 
                                            parent, 
                                            Clutter.BindConstraint.BindType.WIDTH, 
                                            0.5)

# Add the constraint to the child actor
child.add_constraint(constraint)

# Show actors
parent.show()
child.show()

# Main loop
Clutter.main()
