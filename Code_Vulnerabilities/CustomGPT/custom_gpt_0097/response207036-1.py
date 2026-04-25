
import clutter

# Initialize Clutter
stage = clutter.Stage()
stage.set_size(800, 600)

# Create parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)
stage.add_child(parent_actor)

# Create child actor
child_actor = clutter.Actor()
child_actor.set_size(200, 150)  # Initial size (can be set to 1/2 parent width)
parent_actor.add_child(child_actor)

# Create a BindConstraint for width
width_constraint = clutter.BindConstraint()
width_constraint.set_source(parent_actor, clutter.bind('width'))
width_constraint.set_target(child_actor, clutter.bind('width'))

# Set child width to 50% of parent width
width_constraint.set_ratio(0.5)
child_actor.add_constraint(width_constraint)

# Show stage
stage.show()
clutter.main()
