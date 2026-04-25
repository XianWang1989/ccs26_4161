
import clutter

# Initialize Clutter
stage = clutter.Stage()
stage.set_size(800, 600)

# Create parent actor
parent = clutter.Actor()
parent.set_size(200, 200)
parent.set_position(100, 100)
stage.add_child(parent)

# Create child actor
child = clutter.Actor()
child.set_size(100, 100)  # Initial size
child.set_position(10, 10)
stage.add_child(child)

# Create a BindConstraint to make the child actor half the width of the parent
bind_constraint = clutter.BindConstraint()
bind_constraint.set_source(parent)
bind_constraint.set_target(child)
bind_constraint.set_property('width')
bind_constraint.set_factor(0.5)  # Set the factor to 0.5 for 50%

# Apply the constraint
child.add_constraint(bind_constraint)

# Show the stage
stage.show_all()
clutter.main()
