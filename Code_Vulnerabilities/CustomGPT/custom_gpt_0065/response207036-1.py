
import clutter

# Create a stage
stage = clutter.Stage()
stage.set_size(800, 600)

# Create parent actor
parent = clutter.Actor()
parent.set_size(400, 300)
parent.set_position(200, 150)  # Center the parent actor
stage.add_child(parent)

# Create child actor
child = clutter.Actor()
child.set_size(200, 150)
child.set_position(0, 0)  # Position it within the parent actor
parent.add_child(child)

# Create a BindConstraint to bind the child's width to half of the parent's width
constraint = clutter.BindConstraint.new(clutter.Actor.Property.WIDTH, parent, clutter.Actor.Property.WIDTH)
constraint.set_scale(0.5)  # Scale factor of 0.5 to make it half
child.add_constraint(constraint)

# Show everything
stage.show_all()
clutter.main()
