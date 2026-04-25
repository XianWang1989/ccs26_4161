
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, Gdk

def on_quit(actor):
    Clutter.main_quit()

# Initialize Clutter
Clutter.init(None)

# Create the main stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title("BindConstraint Example")
stage.connect("destroy", on_quit)
stage.show()

# Create the parent actor
parent_actor = Clutter.Actor.new()
parent_actor.set_size(400, 300)
parent_actor.set_position(200, 150)
parent_actor.set_background_color(Clutter.Color.from_rgb(0, 0, 255))  # Blue
stage.add_child(parent_actor)

# Create the child actor
child_actor = Clutter.Actor.new()
child_actor.set_size(100, 100)  # Initial size
child_actor.set_position(0, 0)
child_actor.set_background_color(Clutter.Color.from_rgb(255, 0, 0))  # Red
parent_actor.add_child(child_actor)

# BindConstraint to keep child width to half of parent's width
def bind_width_constraint(source, target):
    width = source.get_width() // 2
    target.set_size(width, target.get_height())

# Apply the custom constraint
bind_width_constraint(parent_actor, child_actor)

# Add a signal to update on parent resize
parent_actor.connect("size-changed", lambda *args: bind_width_constraint(parent_actor, child_actor))

# Show all actors
stage.show_all()

# Start the main loop
Clutter.main()
