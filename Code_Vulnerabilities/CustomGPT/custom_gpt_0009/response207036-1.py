
import clutter

# Initialize Clutter
stage = clutter.Stage()
stage.set_size(800, 600)
stage.set_title("Size Constraint Example")

# Create parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_background_color(clutter.Color(0, 0, 255, 255))  # Blue color
stage.add_child(parent_actor)

# Create child actor
child_actor = clutter.Actor()
child_actor.set_size(200, 150)
child_actor.set_position(0, 0)
child_actor.set_background_color(clutter.Color(255, 0, 0, 255))  # Red color
parent_actor.add_child(child_actor)

# Create a bind constraint to maintain 50% of parent's width
bind_constraint = clutter.BindConstraint()
bind_constraint.set_target(parent_actor)
bind_constraint.set_property("width")
bind_constraint.set_value(clutter.BindConstraintValueType.PERCENTAGE, 50)  # 50%

# Attach the constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Show the stage
stage.show_all()
clutter.main()
