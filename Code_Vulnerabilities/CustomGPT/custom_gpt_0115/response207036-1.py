
import clutter

def main():
    # Initialize Clutter
    stage = clutter.Stage()
    stage.set_size(400, 400)
    stage.set_title("BindConstraint Example")

    # Create a parent actor
    parent_actor = clutter.Actor()
    parent_actor.set_size(200, 200)
    parent_actor.set_position(100, 100)
    stage.add_child(parent_actor)

    # Create a child actor
    child_actor = clutter.Actor()
    child_actor.set_size(100, 100)  # Initial size
    child_actor.set_position(0, 0)
    parent_actor.add_child(child_actor)

    # Create a BindConstraint to make child width half of parent width
    bind_constraint = clutter.BindConstraint.new(
        clutter.BindConstraintSource.new(parent_actor, clutter.BIND_TYPE_WIDTH),
        clutter.BindConstraintTarget.new(child_actor, clutter.BIND_TYPE_WIDTH),
        clutter.BindConstraintOperation.MULTIPLY, 0.5
    )

    # Apply the constraint
    child_actor.add_constraint(bind_constraint)

    # Show the stage
    stage.show_all()
    clutter.main()

if __name__ == "__main__":
    main()
