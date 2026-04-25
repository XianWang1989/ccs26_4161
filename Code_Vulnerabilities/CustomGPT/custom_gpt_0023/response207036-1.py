
import clutter

# Initialize Clutter
stage = clutter.Stage()
stage.set_size(800, 600)
stage.show()

# Create the parent actor
parent = clutter.Actor()
parent.set_size(400, 300)
parent.set_position(200, 150)
parent.set_background_color(clutter.Color.red)
stage.add_child(parent)

# Create the child actor
child = clutter.Actor()
child.set_size(100, 100)  # Initial size
child.set_position(50, 50)
child.set_background_color(clutter.Color.blue)
parent.add_child(child)

# Create a BindConstraint to bind the child's width to half of the parent's width
bind_constraint = clutter.BindConstraint()
bind_constraint.set_source(parent)
bind_constraint.set_target(child)
bind_constraint.set_property('width', 'width')
bind_constraint.set_value(0.5)  # Set to 50%

# Apply the BindConstraint
child.add_constraint(bind_constraint)

# Start the Clutter main loop
clutter.main()
