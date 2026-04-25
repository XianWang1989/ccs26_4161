
import clutter

# Initialize the Clutter stage
stage = clutter.Stage.new()
stage.set_size(800, 600)

# Create a parent actor
parent_actor = clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
stage.add_child(parent_actor)

# Create a child actor
child_actor = clutter.Actor.new()
child_actor.set_color(clutter.Color.red)
child_actor.set_size(0, 0)  # Initial size (will be constrained)
parent_actor.add_child(child_actor)

# Function to bind child's width to half of parent's width
def bind_size():
    bind_width = clutter.BindConstraint.new()
    bind_width.set_source(parent_actor)  # The source actor (parent)
    bind_width.set_target(child_actor)   # The target actor (child)
    bind_width.set_property("width", 0.5)  # Bind width to 50% of parent's width
    child_actor.add_constraint(bind_width)

# Call the function to set up the binding
bind_size()

# Show the stage
stage.show_all()
clutter.main()
