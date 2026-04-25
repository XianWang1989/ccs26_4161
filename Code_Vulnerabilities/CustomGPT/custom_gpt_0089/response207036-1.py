
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
child_actor.set_color(clutter.Color(255, 0, 0, 255))  # Red color
parent_actor.add_child(child_actor)

# Create a BindConstraint to bind the child's width
bind_constraint = clutter.BindConstraint()
bind_constraint.set_source(parent_actor)
bind_constraint.set_property("width")
bind_constraint.set_target_property("width")
bind_constraint.set_scaling(0.5)  # Set scaling to 50%

# Add the constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Show the stage
stage.show_all()
stage.set_event_buffering(False)
clutter.main()
