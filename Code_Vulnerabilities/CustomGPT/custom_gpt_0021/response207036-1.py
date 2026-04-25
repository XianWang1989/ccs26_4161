
import clutter

def main():
    stage = clutter.Stage()
    stage.set_size(800, 600)

    # Parent actor
    parent_actor = clutter.Actor()
    parent_actor.set_size(400, 200)
    parent_actor.set_position(100, 100)
    parent_actor.set_background_color(clutter.Color(0, 0, 255, 255))  # Blue
    stage.add_child(parent_actor)

    # Child actor
    child_actor = clutter.Actor()
    child_actor.set_size(200, 100)
    child_actor.set_position(20, 20)
    child_actor.set_background_color(clutter.Color(255, 0, 0, 255))  # Red
    parent_actor.add_child(child_actor)

    # BindConstraint to keep child at half the width of parent
    bind_constraint = clutter.BindConstraint.new(
        child_actor,
        clutter.BindConstraintTarget.WIDTH,
        parent_actor,
        clutter.BindConstraintTarget.WIDTH,
        0.5  # Proportion
    )
    child_actor.add_constraint(bind_constraint)

    # Show the stage
    stage.show_all()
    clutter.main()

if __name__ == '__main__':
    main()
