
import clutter

def create_actor_with_constraints():
    stage = clutter.Stage()
    stage.set_size(800, 600)

    parent_actor = clutter.Actor()
    parent_actor.set_size(400, 300)
    parent_actor.set_position(100, 100)
    stage.add_child(parent_actor)

    child_actor = clutter.Actor()
    child_actor.set_size(200, 150)  # Initial size; will be updated by constraint
    child_actor.set_position(50, 50)
    parent_actor.add_child(child_actor)

    # Create a BindConstraint to bind child's width to half of parent's width
    bind_constraint = clutter.BindConstraint(child_actor, clutter.BindConstraintTarget.WIDTH, parent_actor, clutter.BindConstraintSource.WIDTH)
    bind_constraint.set_value(0.5)  # Scale to 50%

    # Add the constraint to the child actor
    child_actor.add_constraint(bind_constraint)

    stage.show_all()
    clutter.main()

if __name__ == "__main__":
    create_actor_with_constraints()
