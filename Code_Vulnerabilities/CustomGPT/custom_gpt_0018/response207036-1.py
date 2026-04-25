
import clutter

# Create a parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)  # Set parent size

# Create a child actor
child_actor = clutter.Actor()

# Set initial size of child actor (1/2 the width of parent)
child_actor.set_size(parent_actor.get_width() // 2, parent_actor.get_height())

# Create a BindConstraint
bind_constraint = clutter.BindConstraint()
bind_constraint.set_target(parent_actor)
# Bind the child's width to half of the parent's width
bind_constraint.set_value("width", parent_actor.get_width() // 2)

# Add the constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Add actors to the stage or container
stage = clutter.Stage()
stage.add_child(parent_actor)
stage.add_child(child_actor)

# Show and start the main loop
stage.show()
clutter.mainloop()
