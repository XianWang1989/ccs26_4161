
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

def main():
    # Initialize Clutter
    Clutter.init(None)

    # Create the main stage
    stage = Clutter.Stage.new()
    stage.set_size(800, 600)
    stage.set_title("BindConstraint Example")
    stage.show()

    # Create the parent actor
    parent_actor = Clutter.Actor.new()
    parent_actor.set_size(400, 200)
    parent_actor.set_position(200, 200)
    parent_actor.set_background_color(Clutter.Color.from_string("blue"))
    stage.add_child(parent_actor)

    # Create the child actor
    child_actor = Clutter.Actor.new()
    child_actor.set_size(200, 200)  # Initial size, will be constrained
    child_actor.set_position(50, 0)
    child_actor.set_background_color(Clutter.Color.from_string("red"))
    parent_actor.add_child(child_actor)

    # Create a BindConstraint to keep the child's width at half of the parent's width
    width_constraint = Clutter.BindConstraint.new(clutter_actor=parent_actor,
                                                   src_property='width',
                                                   scaling_factor=0.5)
    child_actor.add_constraint(width_constraint)

    # Show all actors
    stage.show_all()

    # Start the main loop
    Clutter.main()

if __name__ == "__main__":
    main()
