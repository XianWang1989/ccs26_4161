
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init(None)

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")
stage.show()

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)  # Width, Height
parent_actor.set_position(200, 150)
parent_actor.set_background_color(Clutter.Color.from_string("blue"))
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(200, 150)  # Initial size
child_actor.set_background_color(Clutter.Color.from_string("red"))
parent_actor.add_child(child_actor)

# Apply a BindConstraint to set the child's width to 50% of the parent's width
bind_constraint = Clutter.BindConstraint.new(child_actor, 
                                              Clutter.BindDimension.WIDTH, 
                                              parent_actor, 
                                              Clutter.BindDimension.WIDTH, 
                                              0.5)  # 50% of parent's width

# Add the constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Show the actors
parent_actor.show()
child_actor.show()

# Start the main loop
Clutter.main()
