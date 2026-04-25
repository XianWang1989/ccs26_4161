
import clutter

# Initialize Clutter
stage = clutter.Stage()
stage.set_size(800, 600)

# Create parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 200)
parent_actor.set_position(100, 100)
stage.add_child(parent_actor)

# Create child actor
child_actor = clutter.Actor()
child_actor.set_size(200, 100)  # Initial size
child_actor.set_position(50, 50)
parent_actor.add_child(child_actor)

# Create a BindConstraint to bind child's width to half of parent's width
constraint = clutter.BindConstraint.new(
    child_actor,
    clutter.BindConstraintTarget.width,
    parent_actor,
    clutter.BindConstraintTarget.width
)
constraint.set_ratio(0.5)  # Set ratio to 1/2

# Add the constraint to the child actor
child_actor.add_constraint(constraint)

# Show the stage
stage.show_all()
clutter.main()
