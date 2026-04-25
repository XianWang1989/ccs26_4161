
import clutter

def proportional_constraint(actor, source_actor):
    # Get the width of the source actor (parent)
    source_width = source_actor.get_width()
    # Set the width of this actor to half of the source actor's width
    new_width = source_width / 2
    actor.set_width(new_width)

# Create a stage and two actors
stage = clutter.Stage()
stage.set_size(800, 600)

parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)
stage.add_child(parent_actor)

child_actor = clutter.Actor()
child_actor.set_size(200, 150)  # Initial size
stage.add_child(child_actor)

# Create and add the BindConstraint
constraint = clutter.BindConstraint.create(child_actor, parent_actor, clutter.BindConstraint.Orientation.WIDTH)
child_actor.add_constraint(constraint)

# Custom update function for proportional resizing
def on_parent_resized(actor):
    proportional_constraint(child_actor, parent_actor)

# Connect to signals for resizing
parent_actor.connect("width-changed", on_parent_resized)
parent_actor.connect("height-changed", on_parent_resized)

# Show the stage
stage.show_all()
clutter.main()
