
import clutter

# Initialize the Clutter stage
stage = clutter.Stage()
stage.set_size(800, 600)

# Create the parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)  # width, height
stage.add_child(parent_actor)

# Create the child actor
child_actor = clutter.Actor()
child_actor.set_size(0, 0)  # Initialize with a size of 0
stage.add_child(child_actor)

# Create the BindConstraint for width, targeting 50% of the parent's width
width_constraint = clutter.BindConstraint.new(
    child_actor,
    clutter.BindConstraintTarget.PARENT,
    clutter.BindConstraintProperty.WIDTH,
    computation_type=0.5)  # 50% of the parent's width

# Add the constraint to the child actor
child_actor.add_constraint(width_constraint)

# Position the actors
parent_actor.set_position(100, 100)
child_actor.set_position(100, 100)

# Show the stage
stage.show_all()
clutter.main()
