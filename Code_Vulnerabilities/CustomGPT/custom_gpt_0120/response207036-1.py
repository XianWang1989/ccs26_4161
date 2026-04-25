
import clutter

# Initialize Clutter
stage = clutter.Stage()
stage.set_size(800, 600)
stage.show()

# Create parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_background_color(clutter.Color.red)
stage.add_child(parent_actor)

# Create child actor
child_actor = clutter.Actor()
child_actor.set_size(200, 150)  # Initial size
child_actor.set_position(50, 50)
child_actor.set_background_color(clutter.Color.blue)
parent_actor.add_child(child_actor)

# Create a BindConstraint to make the child actor half the width of the parent
bind_constraint = clutter.BindConstraint()
bind_constraint.set_source(parent_actor)
bind_constraint.set_target(child_actor)

# Constrain the child actor's width to be half of the parent's width
bind_constraint.set_property('width', clutter.ClampParam(0.5, 0))

# Apply the constraint
child_actor.add_constraint(bind_constraint)

# Show the stage
clutter.main()
