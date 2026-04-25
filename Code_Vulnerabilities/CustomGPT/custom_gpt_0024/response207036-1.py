
import clutter

def create_constrained_actor():
    stage = clutter.Stage()
    stage.set_size(800, 600)

    # Create parent actor
    parent_actor = clutter.Actor()
    parent_actor.set_size(400, 300)
    parent_actor.set_position(200, 150)
    stage.add_child(parent_actor)

    # Create child actor
    child_actor = clutter.Actor()
    child_actor.set_size(200, 150)  # Initial size
    child_actor.set_position(0, 0)
    parent_actor.add_child(child_actor)

    # Create BindConstraint to set child width to 1/2 of parent's width
    width_constraint = clutter.BindConstraint.new(
        clutter.BindTarget("width"),   # Bind target is width
        clutter.BindMode.SET,           # Set mode
        parent_actor,                   # Source actor
        0.5                              # Proportion (50%)
    )

    # Add the constraint to the child actor
    child_actor.add_constraint(width_constraint)

    # Show the stage
    stage.show()

    return stage

if __name__ == "__main__":
    stage = create_constrained_actor()
    clutter.main()
