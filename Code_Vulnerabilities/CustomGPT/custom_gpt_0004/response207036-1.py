
import clutter

# Initialize Clutter
clutter.init([])

# Create a stage
stage = clutter.Stage.new()
stage.set_size(800, 600)

# Create parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
stage.add_child(parent_actor)

# Create child actor
child_actor = clutter.Actor()
child_actor.set_size(200, 150)  # Initial size
child_actor.set_position(100, 75)
stage.add_child(child_actor)

# Define a factor for proportion (1/2)
factor = 0.5

# Create BindConstraint to bind the child's width to half of the parent's width
bind_constraint_width = clutter.BindConstraint.new(
    parent_actor, 
    clutter.BindFlags.WIDTH, 
    clutter.BindFlags.WIDTH, 
    factor
)

# Create BindConstraint to bind the child's height to half of the parent's height
bind_constraint_height = clutter.BindConstraint.new(
    parent_actor, 
    clutter.BindFlags.HEIGHT, 
    clutter.BindFlags.HEIGHT, 
    factor
)

# Add the constraints to the child actor
child_actor.add_constraint(bind_constraint_width)
child_actor.add_constraint(bind_constraint_height)

# Show the stage
stage.show_all()
clutter.main()
