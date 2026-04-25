
import clutter

# Initialize Clutter
stage = clutter.Stage.new()
stage.set_size(800, 600)

# Create parent actor
parent_actor = clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
stage.add_child(parent_actor)

# Create the child actor
child_actor = clutter.Actor.new()
child_actor.set_size(100, 100)  # Initial size
child_actor.set_position(50, 50)
parent_actor.add_child(child_actor)

# Create BindConstraint to keep child_actor width at half of parent_actor width
bind_constraint = clutter.BindConstraint.new(clutter.BindConstraintTarget.WIDTH)
bind_constraint.set_target(parent_actor)

# Apply scaling factor of 0.5 for width
bind_constraint.set_factor(0.5)

# Add the BindConstraint to the child actor
child_actor.add_constraint(bind_constraint)

# Show the stage
stage.show_all()
clutter.main()
