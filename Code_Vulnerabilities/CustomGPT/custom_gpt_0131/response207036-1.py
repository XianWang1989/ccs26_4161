
import clutter

# Initialize Clutter
stage = clutter.Stage()
stage.set_size(800, 600)

# Create the parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_color(clutter.color_from_string("blue"))
stage.add_child(parent_actor)

# Create the child actor
child_actor = clutter.Actor()
child_actor.set_size(200, 150)  # Initial size will be overridden by binding
child_actor.set_color(clutter.color_from_string("red"))
stage.add_child(child_actor)

# Create a BindConstraint to make the child actor half the width of the parent actor
bind_constraint = clutter.BindConstraint()
bind_constraint.set_source(parent_actor)
bind_constraint.set_property_name("width")
bind_constraint.set_target_property("width")
bind_constraint.set_scale(0.5)  # Set the proportion to 1/2 (50%)

# Add the BindConstraint to the child actor
child_actor.add_constraint(bind_constraint)

# Show the stage
stage.show()
clutter.main()
