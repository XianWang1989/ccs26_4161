
import clutter

def main():
    stage = clutter.Stage.new()
    stage.set_size(800, 600)

    parent_actor = clutter.Actor.new()
    parent_actor.set_size(200, 200)
    parent_actor.set_position(100, 100)
    parent_actor.set_color(clutter.Color(255, 0, 0, 255))  # Red
    stage.add_child(parent_actor)

    child_actor = clutter.Actor.new()
    child_actor.set_size(100, 100)  # Initial size
    child_actor.set_position(50, 50)
    child_actor.set_color(clutter.Color(0, 0, 255, 255))  # Blue
    parent_actor.add_child(child_actor)

    # Creating a BindConstraint to constrain the width to half the parent's width
    width_constraint = clutter.BindConstraint()
    width_constraint.set_source(parent_actor, clutter.BindingType.WIDTH)  # Bind to parent's width
    width_constraint.set_target(child_actor, clutter.BindingType.WIDTH)  # Target child's width
    width_constraint.set_factor(0.5)  # Set the factor to 0.5

    # Add the constraint to the child actor
    child_actor.add_constraint(width_constraint)

    stage.show_all()
    clutter.main()

if __name__ == "__main__":
    main()
