
import clutter

# Initialize Clutter
stage = clutter.Stage()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")

# Create a parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_background_color(clutter.Color(red=255, green=0, blue=0, alpha=255))  # Red
stage.add_child(parent_actor)

# Create a child actor
child_actor = clutter.Actor()
child_actor.set_size(100, 100)
child_actor.set_position(50, 50)
child_actor.set_background_color(clutter.Color(red=0, green=0, blue=255, alpha=255))  # Blue
parent_actor.add_child(child_actor)

# Create a BindConstraint to make the child's width half of the parent's width
bind_constraint = clutter.BindConstraint()
bind_constraint.set_target(parent_actor)
bind_constraint.set_target_size(0.5)  # The target size as a proportion (0.5 means half)
bind_constraint.set_property("width")
child_actor.add_constraint(bind_constraint)

# Show the stage
stage.show_all()
clutter.main()
