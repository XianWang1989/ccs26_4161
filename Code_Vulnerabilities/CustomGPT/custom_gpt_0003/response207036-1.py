
import clutter

# Initialize the Clutter stage
stage = clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")

# Create the parent actor
parent_actor = clutter.Actor.new()
parent_actor.set_size(400, 300)  # Set size of the parent actor
parent_actor.set_color(clutter.Color(255, 0, 0, 255))  # Red color for visibility
stage.add_child(parent_actor)

# Create the child actor
child_actor = clutter.Actor.new()
child_actor.set_size(200, 150)  # Initial size of the child actor
child_actor.set_color(clutter.Color(0, 0, 255, 255))  # Blue color for visibility
stage.add_child(child_actor)

# Create a BindConstraint to bind child_actor's width to half of parent's width
width_constraint = clutter.BindConstraint.new(parent_actor, 
                                               clutter.BindConstraintType.WIDTH, 
                                               0.5)  # 0.5 means 50% of parent's width
child_actor.add_constraint(width_constraint)

# Show the stage
stage.show_all()

# Start the main loop
clutter.main()
