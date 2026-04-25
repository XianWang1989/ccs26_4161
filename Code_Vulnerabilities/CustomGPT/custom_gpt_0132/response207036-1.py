
import clutter

# Initialize Clutter
stage = clutter.Stage()
stage.set_size(800, 600)

# Create a parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_position(100, 100)
stage.add_child(parent_actor)

# Create a child actor
child_actor = clutter.Actor()
child_actor.set_size(100, 100)
child_actor.set_position(10, 10)
parent_actor.add_child(child_actor)

# Create a bind constraint for width
def update_child_width(_constraint, source_actor, target_actor):
    parent_width = source_actor.get_width()
    target_actor.set_size(parent_width / 2, target_actor.get_height())

# Create the BindConstraint
bind_constraint = clutter.BindConstraint.new(child_actor, parent_actor,
                                              clutter.BindConstraintProperty.WIDTH)

# Add the constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Connect signal to update child width proportionally
parent_actor.connect('notify::width', update_child_width, child_actor)

# Show the stage
stage.show_all()
clutter.main()
