
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init(None)

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.show()

# Create parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)  # Set parent's size
parent_actor.set_color(Clutter.Color(255, 0, 0, 255))  # Red color
stage.add_child(parent_actor)

# Create child actor
child_actor = Clutter.Actor.new()
child_actor.set_color(Clutter.Color(0, 0, 255, 255))  # Blue color

# Add the child to the parent
parent_actor.add_child(child_actor)

# Create a bind constraint to keep the child's width to half of the parent's width
constraint = Clutter.BindConstraint.new(child_actor, parent_actor, 
                                         "width", "width", 
                                         0.5)  # 0.5 for 50%
child_actor.add_constraint(constraint)

# Show both actors
parent_actor.show()
child_actor.show()

# Start the main loop
Clutter.main()
