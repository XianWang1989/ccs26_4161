
import clutter

# Initialize Clutter
stage = clutter.Stage()
stage.set_size(800, 600)

# Create a parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)
stage.add_child(parent_actor)

# Create a child actor
child_actor = clutter.Actor()
child_actor.set_size(0, 0)  # Initial size set to zero
stage.add_child(child_actor)

# Create a BindConstraint that binds the child actor's width to half of the parent's width
bind_constraint = clutter.BindConstraint(
    clutter.BindConstraint.create(child_actor, 
                                   clutter.BindConstraintType.WIDTH, 
                                   parent_actor, 
                                   clutter.BindConstraintType.WIDTH)
)

# Set the child actor to 50% of the parent's width
bind_constraint.set_value(0.5)  # This sets the binding to 50%

# Now apply the constraint
child_actor.add_constraint(bind_constraint)

# Set positions for visibility
parent_actor.set_position(100, 100)
child_actor.set_position(100, 200)

# Show the stage
stage.show_all()
clutter.main()
