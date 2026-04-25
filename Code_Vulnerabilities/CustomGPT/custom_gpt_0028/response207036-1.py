
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_color(Clutter.Color.new(0, 255, 0, 255))  # Green
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor()
child_actor.set_size(100, 100)
child_actor.set_color(Clutter.Color.new(255, 0, 0, 255))  # Red
stage.add_child(child_actor)

# Bind the child's width to half of the parent's width using a BindConstraint
def scale_child_width(constraint, actor):
    parent_width = parent_actor.get_width()
    new_width = parent_width / 2
    child_actor.set_width(new_width)

# Create a BindConstraint for the width
bind_constraint = Clutter.BindConstraint.new(parent_actor, Clutter.BindConstraintFlags.WIDTH)
bind_constraint.connect('notify::value', scale_child_width)
child_actor.add_constraint(bind_constraint)

# Show actors
parent_actor.show()
child_actor.show()

# Start the Clutter main loop
Clutter.main()
