
import clutter

# Initialize Clutter
clutter.init([])

# Create the main stage
stage = clutter.Stage.new()
stage.set_size(800, 600)
stage.show()

# Create a parent actor
parent = clutter.Actor.new()
parent.set_size(400, 300)
parent.set_position(200, 150)
parent.set_color(clutter.Color(255, 0, 0, 255))  # Red
stage.add_child(parent)

# Create a child actor
child = clutter.Actor.new()
child.set_size(200, 150)  # Initial size
child.set_position(50, 75)  # Relative position within parent
child.set_color(clutter.Color(0, 0, 255, 255))  # Blue
parent.add_child(child)

# Create a BindConstraint to keep the child's width at half of parent's width
bind_constraint = clutter.BindConstraint.new(clutter.BindDimension.WIDTH, parent, clutter.BindDimension.WIDTH)
bind_constraint.set_ratio(0.5)  # Set ratio to 0.5 (half)
child.add_constraint(bind_constraint)

# Show the stage
clutter.main()
