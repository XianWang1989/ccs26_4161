
import clutter

# Create a stage
stage = clutter.Stage()
stage.set_size(800, 600)

# Create parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(200, 100)
parent_actor.set_position(100, 100)
parent_actor.set_color(clutter.Color(255, 0, 0, 255))  # Red color
stage.add_child(parent_actor)

# Create child actor
child_actor = clutter.Actor()
child_actor.set_size(100, 50)  # Initial size
child_actor.set_position(50, 25)
child_actor.set_color(clutter.Color(0, 0, 255, 255))  # Blue color
stage.add_child(child_actor)

# Create a BindConstraint to bind the child's width to half of parent's width
bind_constraint = clutter.BindConstraint.create(child_actor, parent_actor, clutter.BindDimension.WIDTH)
# Set the child width to be half of the parent's width
bind_constraint.set_multiplier(0.5)

# Add the constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Show the stage
stage.show_all()
clutter.main()
