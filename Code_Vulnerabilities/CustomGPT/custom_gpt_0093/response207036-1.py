
import clutter

# Initialize the Clutter stage
stage = clutter.Stage()
stage.set_size(800, 600)
stage.show()

# Create a parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_background_color(clutter.Color.from_string("blue"))

# Create a child actor
child_actor = clutter.Actor()
child_actor.set_size(200, 150)  # initial size
child_actor.set_position(0, 0)
child_actor.set_background_color(clutter.Color.from_string("red"))

# Add both actors to the stage
stage.add_child(parent_actor)
parent_actor.add_child(child_actor)

# Create a BindConstraint to constrain the width of the child actor
# to 50% of the parent's width
constraint = clutter.BindConstraint()
constraint.set_target(parent_actor)
constraint.set_property("width", 0.5)  # 50% of parent's width

# Add the constraint to the child actor
child_actor.add_constraint(constraint)

# Show the actors
parent_actor.show()
child_actor.show()

# Start the mainloop to keep the stage open
clutter.main()
