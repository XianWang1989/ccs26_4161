
import clutter

def main():
    stage = clutter.Stage()
    stage.set_size(800, 600)
    stage.set_title("BindConstraint Example")

    parent_actor = clutter.Actor()
    parent_actor.set_size(400, 200)
    parent_actor.set_position(200, 200)  # Center it in the stage
    stage.add_actor(parent_actor)

    child_actor = clutter.Actor()
    child_actor.set_size(200, 100)
    child_actor.set_position(0, 0)  # Position at the top-left of the parent
    parent_actor.add_actor(child_actor)

    # Create BindConstraints
    width_constraint = clutter.BindConstraint.new(child_actor, clutter.BindConstraintDimension.WIDTH, parent_actor, clutter.BindConstraintDimension.WIDTH, 0.5)
    height_constraint = clutter.BindConstraint.new(child_actor, clutter.BindConstraintDimension.HEIGHT, parent_actor, clutter.BindConstraintDimension.HEIGHT, 0.5)

    # Add constraints to the child actor
    child_actor.add_constraint(width_constraint)
    child_actor.add_constraint(height_constraint)

    stage.show_all()
    clutter.main()

if __name__ == "__main__":
    main()
