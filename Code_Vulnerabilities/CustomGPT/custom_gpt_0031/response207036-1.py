
import clutter

def main():
    stage = clutter.Stage()
    stage.set_size(800, 600)
    stage.set_title("BindConstraint Example")
    stage.show()

    # Create parent actor
    parent_actor = clutter.Actor()
    parent_actor.set_size(400, 300)
    parent_actor.set_position(200, 150)
    parent_actor.set_background_color(clutter.color_from_string("blue"))
    stage.add_child(parent_actor)

    # Create child actor
    child_actor = clutter.Actor()
    child_actor.set_size(200, 150)
    child_actor.set_background_color(clutter.color_from_string("red"))
    parent_actor.add_child(child_actor)

    # Create BindConstraint to bind child's width to half of parent's width
    bind_constraint = clutter.BindConstraint.new(parent_actor, clutter.BIND_WIDTH)
    bind_constraint.set_expression(clutter.ConstraintExpression.new_expression(
        "width / 2", child_actor.get_width()
    ))
    child_actor.add_constraint(bind_constraint)

    stage.show_all()
    clutter.main()

if __name__ == "__main__":
    main()
