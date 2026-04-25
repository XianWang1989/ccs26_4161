
import clutter

# Initialize Clutter
clutter.init(None)

# Create a new stage
stage = clutter.Stage()
stage.set_size(800, 600)
stage.set_title("Size Constraint Example")

# Create a parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_background_color(clutter.Color.from_string("blue"))

# Create a child actor
child_actor = clutter.Actor()
child_actor.set_size(200, 150)  # Initial size
child_actor.set_position(0, 0)
child_actor.set_background_color(clutter.Color.from_string("red"))

# Add parent and child to the stage
stage.add_child(parent_actor)
parent_actor.add_child(child_actor)

# Create a BindConstraint to keep the child's width at half of the parent's width
bind_constraint = clutter.BindConstraint(child_actor, clutter.BindConstraint.BIND_WIDTH, parent_actor, clutter.BindConstraint.BIND_WIDTH)
bind_constraint.set_scale(0.5)  # Set the scale to 0.5

# Add the constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Show the stage
stage.show()
clutter.main()
