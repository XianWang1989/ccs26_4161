
import clutter

# Initialize the Clutter stage
stage = clutter.Stage()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")

# Create the parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(200, 100)  # Width, Height
parent_actor.set_position(100, 250)
stage.add_child(parent_actor)

# Create the child actor
child_actor = clutter.Actor()
child_actor.set_size(100, 50)  # Initial size
child_actor.set_position(50, 25)
stage.add_child(child_actor)

# Create a BindConstraint to bind child's width to half of parent's width
def on_parent_size_changed(actor):
    parent_width = actor.get_width()
    child_new_width = parent_width / 2.0
    child_actor.set_size(child_new_width, child_actor.get_height())

# Connect the signal to detect changes in the parent's size
parent_actor.connect('size-changed', on_parent_size_changed)

# Show the stage
stage.show_all()
# Start the main loop
clutter.main()
