
import clutter

# Initialize Clutter
stage = clutter.Stage()
stage.set_size(800, 600)

# Create a parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_background_color(clutter.Color(255, 0, 0, 255))  # Red background
stage.add_child(parent_actor)

# Create a child actor
child_actor = clutter.Actor()
child_actor.set_size(200, 150)  # Initial size
child_actor.set_position(50, 50)
child_actor.set_background_color(clutter.Color(0, 0, 255, 255))  # Blue background
parent_actor.add_child(child_actor)

# Create a BindConstraint to constrain the child's width to 1/2 of the parent's width
bind_constraint = clutter.BindConstraint.create("width", parent_actor, "width", clutter.BindConstraint.Orientation.HORIZONTAL)
child_actor.add_constraint(bind_constraint)

# Define a custom function to update the child's width to half of parent's
def update_child_size():
    parent_width = parent_actor.get_width()
    child_actor.set_size(parent_width / 2, child_actor.get_height())

# Connect the signal to update child size whenever parent size changes
parent_actor.connect("notify::width", lambda actor, param: update_child_size())

# Show the stage
stage.show_all()

# Main loop
clutter.main()
