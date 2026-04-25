
import clutter

# Create a new stage
stage = clutter.Stage.new()

# Create parent actor
parent_actor = clutter.Actor.new()
parent_actor.set_size(400, 300)  # Width, Height
stage.add_child(parent_actor)

# Create child actor
child_actor = clutter.Actor.new()
child_actor.set_size(200, 150)  # Initial size
parent_actor.add_child(child_actor)

# Set up a bind constraint to constrain the child's width to half of the parent's width
def bind_constraint_func(child, property, parent):
    # Calculate the new width as half of the parent’s width
    new_width = parent.get_width() / 2
    return new_width

bind_constraint = clutter.BindConstraint.new(parent_actor, 
                                              clutter.BindConstraintProperty.WIDTH, 
                                              bind_constraint_func, 
                                              None)

# Apply the bind constraint
child_actor.add_constraint(bind_constraint)

# Show the stage
stage.show_all()

# Main loop
clutter.main()
