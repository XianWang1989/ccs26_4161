
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

# Initialize Clutter
Clutter.init([])

# Create a stage and two actors
stage = Clutter.Stage(width=800, height=600)
stage.set_title("BindConstraint Example")
stage.show()

parent_actor = Clutter.Actor(width=400, height=300)
parent_actor.set_position(200, 150)
parent_actor.set_background_color(Clutter.color_from_rgb(255, 0, 0))
stage.add_child(parent_actor)

child_actor = Clutter.Actor(width=200, height=150)
child_actor.set_position(0, 0)
child_actor.set_background_color(Clutter.color_from_rgb(0, 0, 255))
parent_actor.add_child(child_actor)

# BindConstraint to make the child actor half the width of the parent
def constrain_size():
    bind_constraint = Clutter.BindConstraint.new(
        child_actor,
        parent_actor,
        Clutter.BindDimension.WIDTH,  # Constrain width
        0.5,                          # Proportion (50%)
        Clutter.BindDimension.WIDTH   # Source dimension
    )
    child_actor.add_constraint(bind_constraint)

constrain_size()

# Start the Clutter main loop
Clutter.main()
