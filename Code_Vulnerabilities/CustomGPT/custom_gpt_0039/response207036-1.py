
import clutter

def main():
    # Initialize Clutter
    stage = clutter.Stage.new()
    stage.set_size(800, 600)
    stage.show()

    # Parent Actor
    parent_actor = clutter.Actor.new()
    parent_actor.set_size(400, 200)
    parent_actor.set_position(200, 200)
    stage.add_child(parent_actor)

    # Child Actor
    child_actor = clutter.Actor.new()
    child_actor.set_size(0, 100)  # Initial size, will be constrained
    child_actor.set_position(0, 0)
    parent_actor.add_child(child_actor)

    # Create a BindConstraint to keep child at 1/2 width of parent
    bind_constraint = clutter.BindConstraint.new(
        clutter.BindConstraintTarget.WIDTH,  # We are binding width
        parent_actor,                         # The source actor
        0.5                                   # Factor to scale
    )

    # Add the constraint to the child actor
    child_actor.add_constraint(bind_constraint)

    # Show actors
    parent_actor.show()
    child_actor.show()

    # Start main loop
    clutter.main()

if __name__ == "__main__":
    main()
