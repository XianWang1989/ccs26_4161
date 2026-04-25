
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

def main():
    # Initialize Clutter
    Clutter.init(None)

    # Create a stage
    stage = Clutter.Stage.new()
    stage.set_size(800, 600)
    stage.show()

    # Create a parent actor
    parent_actor = Clutter.Actor.new()
    parent_actor.set_size(400, 300)
    parent_actor.set_position(200, 150)
    stage.add_child(parent_actor)

    # Create a child actor
    child_actor = Clutter.Actor.new()
    child_actor.set_size(0, 0)  # Initialize with zero size
    child_actor.set_position(0, 0)
    parent_actor.add_child(child_actor)

    # Create a BindConstraint
    width_constraint = Clutter.BindConstraint.new(
        child_actor, 
        Clutter.BindParam.WIDTH, 
        parent_actor, 
        Clutter.BindParam.WIDTH,
        0.5  # Set to half the width of the parent
    )

    # Apply the constraint
    child_actor.add_constraint(width_constraint)

    # Show actors
    parent_actor.show()
    child_actor.show()

    # Start the main loop
    Clutter.main()

if __name__ == "__main__":
    main()
