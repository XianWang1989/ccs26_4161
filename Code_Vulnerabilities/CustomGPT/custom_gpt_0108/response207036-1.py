
import clutter

# Create a function to update the size of the child actor
def update_child_size(child, parent):
    parent_width = parent.get_width()
    new_width = parent_width / 2  # Set child width to half of parent's width
    child.set_size(new_width, child.get_height())

# Initialize Clutter
stage = clutter.Stage()
stage.set_size(800, 600)

# Create parent actor
parent = clutter.Actor()
parent.set_size(400, 300)
parent.set_position(200, 150)
stage.add_child(parent)

# Create child actor
child = clutter.Actor()
child.set_size(100, 100)
child.set_position(0, 0)  # Position it relative to parent
parent.add_child(child)

# Create BindConstraint to link the child actor's size to the parent's
bind_constraint = clutter.BindConstraint(child)
bind_constraint.set_target(parent)

# Connect the "notify::size" signal of the parent to update the child's size
parent.connect("notify::size", lambda *_: update_child_size(child, parent))

# Show everything
stage.show_all()

# Start the main loop
clutter.main()
