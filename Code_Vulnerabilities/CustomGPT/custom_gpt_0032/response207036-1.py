
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.show()

# Create the parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_color(Clutter.Color.new(255, 0, 0, 255))  # Red
stage.add_child(parent_actor)

# Create the child actor
child_actor = Clutter.Actor.new()
child_actor.set_color(Clutter.Color.new(0, 255, 0, 255))  # Green
child_actor.set_size(200, 150)  # Initial size
stage.add_child(child_actor)

# Create a BindConstraint to adjust the child's width to 1/2 of the parent's width
width_constraint = Clutter.BindConstraint.new(
    parent_actor, 
    Clutter.BindDimension.WIDTH, 
    Clutter.BindDimension.WIDTH, 
    0.5  # Proportional binding factor
)
child_actor.add_constraint(width_constraint)

# Show the stage
Clutter.main()
