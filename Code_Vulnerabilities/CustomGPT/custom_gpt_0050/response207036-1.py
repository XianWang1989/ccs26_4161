
import clutter

# Initialize Clutter
stage = clutter.Stage()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")

# Create parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_background_color(clutter.Color(0, 0, 255, 255))  # Blue
stage.add_child(parent_actor)

# Create child actor
child_actor = clutter.Actor()
child_actor.set_size(100, 150)  # Initial size
child_actor.set_position(50, 75)
child_actor.set_background_color(clutter.Color(255, 0, 0, 255))  # Red
stage.add_child(child_actor)

# Create a BindConstraint to bind child's width to half of parent's width
width_constraint = clutter.BindConstraint.new(
    clutter.BindDimension.WIDTH,   # Dimension to bind
    parent_actor,                   # Source actor
    clutter.BindDimension.WIDTH,    # Source dimension
    0.5                             # Ratio (1/2)
)

# Add the constraint to the child actor
child_actor.add_constraint(width_constraint)

# Show the stage
stage.show_all()

clutter.main()
