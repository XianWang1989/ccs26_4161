
import clutter

# Initialize Clutter
stage = clutter.Stage()
stage.set_size(800, 600)

# Create a parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
stage.add_child(parent_actor)

# Create a child actor
child_actor = clutter.Actor()
child_actor.set_size(200, 150)
child_actor.set_position(10, 10)
parent_actor.add_child(child_actor)

# Create a BindConstraint to set the child's width to half of the parent's width
width_constraint = clutter.BindConstraint()
width_constraint.set_property("source", parent_actor)
width_constraint.set_property("target", child_actor)
width_constraint.set_property("property", "width")

# Set the scale to 0.5 (half the width)
width_constraint.set_property("factor", 0.5)

# Add the constraint to the child actor
child_actor.add_constraint(width_constraint)

# Show the stage
stage.show()
clutter.main()
