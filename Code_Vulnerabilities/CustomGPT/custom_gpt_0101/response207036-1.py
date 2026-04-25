
import clutter

# Create a stage
stage = clutter.Stage.new(800, 600)
stage.set_title("BindConstraint Example")

# Create a parent actor
parent = clutter.Actor.new()
parent.set_size(400, 300)
stage.add_child(parent)

# Create a child actor
child = clutter.Actor.new()
child.set_background_color(clutter.Color('blue'))
parent.add_child(child)

# Create a bind constraint to keep the child's width at 50% of the parent's width
bind_constraint = clutter.BindConstraint.new(
    clutter.BindConstraintType.WIDTH,
    clutter.BindConstraintSource.new(parent, clutter.BindConstraintType.WIDTH),
    0.5  # 50%
)

# Add the constraint to the child
child.add_constraint(bind_constraint)

# Show all actors
stage.show_all()

# Start the main loop
clutter.main()
