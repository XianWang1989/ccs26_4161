
import clutter

# Create the main stage
stage = clutter.Stage.new(800, 600)
stage.set_title("BindConstraint Example")

# Create the parent actor
parent_actor = clutter.Actor.new()
parent_actor.set_size(400, 400)
parent_actor.set_position(200, 100)
parent_actor.set_background_color(clutter.Color(50, 50, 50, 255))
stage.add_child(parent_actor)

# Create the child actor
child_actor = clutter.Actor.new()
child_actor.set_background_color(clutter.Color(200, 0, 0, 255))
child_actor.set_size(100, 100)  # Initial size, will be constrained
parent_actor.add_child(child_actor)

# BindConstraint to constrain the width of the child actor to half of the parent's width
bind_constraint = clutter.BindConstraint.new(parent_actor, clutter.BindDimension.WIDTH, 0.5)
child_actor.add_constraint(bind_constraint)

# Show the stage
stage.show_all()
clutter.main()
