
import clutter

# Initialize Clutter
clutter.init([])

# Create a stage
stage = clutter.Stage()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")

# Create parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
stage.add_child(parent_actor)

# Create child actor
child_actor = clutter.Actor()
child_actor.set_size(0, 0)  # Initial size will be set by constraint
child_actor.set_position(50, 50)  # Position it inside the parent
parent_actor.add_child(child_actor)

# Create a bind constraint to keep the child actor's width to 1/2 of parent's width
width_constraint = clutter.BindConstraint.new(clutter.BindConstraintType.BIND_WIDTH, parent_actor, clutter.BindConstraintWeight.DIRECT)
width_constraint.set_factor(0.5)  # 50% of the parent's width
child_actor.add_constraint(width_constraint)

# Show the stage
stage.show_all()
clutter.main()
