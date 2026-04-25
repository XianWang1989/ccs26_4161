
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

def create_bounding_actors():
    # Initialize Clutter
    Clutter.init(None)

    # Create the main stage
    stage = Clutter.Stage.new()
    stage.set_size(800, 600)
    stage.set_title("BindConstraint Example")
    stage.show()

    # Create the parent actor
    parent_actor = Clutter.Actor.new()
    parent_actor.set_size(400, 300)
    parent_actor.set_background_color(Clutter.Color.new(255, 0, 0, 255))  # Red
    stage.add_child(parent_actor)

    # Create the child actor
    child_actor = Clutter.Actor.new()
    child_actor.set_size(200, 150)
    child_actor.set_background_color(Clutter.Color.new(0, 0, 255, 255))  # Blue
    parent_actor.add_child(child_actor)

    # Create BindConstraint to keep child at 1/2 the width of parent
    bind_constraint = Clutter.BindConstraint.new(child_actor, Clutter.BindFlags.WIDTH, parent_actor, Clutter.BindFlags.WIDTH)
    bind_constraint.set_ratio(0.5, 1.0)  # Set width to 50% of parent width
    child_actor.add_constraint(bind_constraint)

    # Show all actors
    stage.show_all()

    # Main loop
    Clutter.main()

if __name__ == '__main__':
    create_bounding_actors()
