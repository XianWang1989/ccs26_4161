
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, Gio

def main():
    Clutter.init([])

    # Create a stage
    stage = Clutter.Stage.new()
    stage.set_size(800, 600)
    stage.set_title("BindConstraint Example")
    stage.show()

    # Create parent actor
    parent_actor = Clutter.Actor.new()
    parent_actor.set_size(400, 400)
    parent_actor.set_position(200, 100)
    parent_actor.set_background_color(Clutter.Color.new(255, 0, 0, 255))  # Red
    stage.add_child(parent_actor)

    # Create child actor
    child_actor = Clutter.Actor.new()
    child_actor.set_size(200, 200)  # Initial size
    child_actor.set_position(100, 100)
    child_actor.set_background_color(Clutter.Color.new(0, 0, 255, 255))  # Blue
    parent_actor.add_child(child_actor)

    # Create a bind constraint to set the child to half the width of the parent
    bind_constraint = Clutter.BindConstraint.new(child_actor, parent_actor, Clutter.BindFlags.WIDTH)

    # Use a multiplier to make the child's width half of the parent's width
    bind_constraint.set_property_ratio(0.5)
    child_actor.add_constraint(bind_constraint)

    # Show the stage
    stage.show_all()

    # Start the main event loop
    Clutter.main()

if __name__ == '__main__':
    main()
