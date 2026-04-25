
import clutter

# Create a stage and two actors
stage = clutter.Stage()
stage.set_size(800, 600)

# Parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(200, 200)
parent_actor.set_position(100, 100)
stage.add_child(parent_actor)

# Child actor
child_actor = clutter.Actor()
child_actor.set_size(100, 100)
child_actor.set_position(50, 50)
stage.add_child(child_actor)

# Function to create a size constraint
def create_proportional_size_constraint(source, target, proportion):
    return clutter.BindConstraint(target, "size", source, "width",
                                   clutter.BindFlags.VALUE | clutter.BindFlags.SIZE,
                                   proportion)

# Bind the size of the child actor to half the width of the parent actor
constraint = create_proportional_size_constraint(parent_actor, child_actor, 0.5)

# Apply the constraint
child_actor.add_constraint(constraint)

# Show the stage
stage.show()
clutter.main()
