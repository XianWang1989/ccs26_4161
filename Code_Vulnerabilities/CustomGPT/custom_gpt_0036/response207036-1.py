
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init([])

# Create a stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")

# Create a parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)  # Set size of parent actor
parent_actor.set_position(200, 150)
parent_actor.set_background_color(Clutter.Color.from_string("blue"))
stage.add_child(parent_actor)

# Create a child actor
child_actor = Clutter.Actor.new()
child_actor.set_background_color(Clutter.Color.from_string("red"))
child_actor.set_size(100, 100)  # Initial size for the child
child_actor.set_position(0, 0)
parent_actor.add_child(child_actor)

# Create a BindConstraint to link the width of the child to 50% of the parent's width
bind_constraint = Clutter.BindConstraint.new(parent_actor, Clutter.BindDimension.WIDTH, 0.5)
# Add the bind constraint to the child actor
child_actor.add_constraint(bind_constraint)

# Show the stage and all actors
stage.show_all()

# Set the main loop
Clutter.Main.loop()

# Cleanup and exit upon window close
def on_destroy(stage):
    Clutter.Main.quit()

stage.connect("destroy", on_destroy)
