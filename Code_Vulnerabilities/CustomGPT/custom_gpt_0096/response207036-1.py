
import clutter

# Initialize Clutter
stage = clutter.Stage()
stage.set_size(800, 600)
stage.show()

# Create the parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
stage.add_child(parent_actor)

# Create the child actor
child_actor = clutter.Actor()
child_actor.set_size(200, 150)
child_actor.set_position(50, 50)
parent_actor.add_child(child_actor)

# Create the BindConstraint to keep the child's width to half of the parent's width
def constrain_actor_size(constraint, actor):
    parent_width = parent_actor.get_width()
    new_width = parent_width / 2
    actor.set_size(new_width, actor.get_height())

# Add the BindConstraint
bind_constraint = clutter.BindConstraint()
bind_constraint.bind(parent_actor, clutter.BIND_WIDTH)
child_actor.add_constraint(bind_constraint)

# Connect the signal for size change
parent_actor.connect("notify::width", lambda a, b: constrain_actor_size(bind_constraint, child_actor))

# Start the main loop
clutter.main()
