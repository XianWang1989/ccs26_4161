
import clutter

def on_size_changed(actor, width, height):
    # Update the size of the child actor to half of the parent's width
    new_width = width / 2
    child_actor.set_size(new_width, height)

# Create a stage
stage = clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")

# Create parent actor
parent_actor = clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
stage.add_child(parent_actor)

# Create child actor
child_actor = clutter.Actor.new()
child_actor.set_size(0, 300)  # Initial size, will be updated
child_actor.set_position(0, 0)
parent_actor.add_child(child_actor)

# Bind constraint to keep child width at half of parent's width
parent_actor.connect("size-changed", on_size_changed)

# Show the stage
stage.show()
clutter.main()
