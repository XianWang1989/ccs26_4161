
import clutter

# Initialize Clutter
stage = clutter.Stage()
stage.set_size(800, 600)

# Create the parent actor
parent = clutter.Actor()
parent.set_size(400, 300)
parent.set_color(clutter.color_from_string("blue"))
stage.add_child(parent)

# Create the child actor
child = clutter.Actor()
child.set_size(200, 150)
child.set_color(clutter.color_from_string("red"))
parent.add_child(child)

# Create a BindConstraint to set the child's width to half of the parent's width
constraint = clutter.BindConstraint.create(
    clutter.BindConstraintBindSize.WIDTH,  # Bind width
    parent,                                   # Source actor (parent)
    clutter.BindConstraintMultiplier(0.5)     # Multiply by 0.5
)

# Add the constraint to the child actor
child.add_constraint(constraint)

# Show the stage
stage.show()
clutter.main()
