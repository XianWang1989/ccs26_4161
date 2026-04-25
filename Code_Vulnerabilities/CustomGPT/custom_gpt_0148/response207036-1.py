
import clutter

# Initialize Clutter
clutter.init()

# Create the main stage
stage = clutter.Stage()
stage.set_size(800, 600)
stage.show()

# Create a parent actor
parent_actor = clutter.Actor()
parent_actor.set_size(400, 400)
parent_actor.set_position(200, 100)
parent_actor.set_background_color(clutter.Color(255, 0, 0, 255))  # Red background
stage.add_child(parent_actor)

# Create a child actor
child_actor = clutter.Actor()
child_actor.set_height(200)  # Set a fixed height
child_actor.set_position(0, 100)
child_actor.set_background_color(clutter.Color(0, 0, 255, 255))  # Blue background

# Create a BindConstraint to bind the child's width to half of the parent's width
width_constraint = clutter.BindConstraint.new(parent_actor, clutter.BindProperty.WIDTH)
width_constraint.set_factor(0.5)  # Set factor to half
child_actor.add_constraint(width_constraint)

# Add the child actor to the parent
parent_actor.add_child(child_actor)

# Show the actors
parent_actor.show()
child_actor.show()

# Start the Clutter main loop
clutter.main()
