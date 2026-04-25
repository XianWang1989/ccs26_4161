
import clutter
import sys

def main():
    # Initialize Clutter
    clutter.init(sys.argv)

    # Create a stage
    stage = clutter.Stage.new()
    stage.set_size(800, 600)
    stage.set_title("BindConstraint Example")

    # Create a parent actor
    parent_actor = clutter.Actor.new()
    parent_actor.set_size(400, 300)
    parent_actor.set_color(clutter.Color(255, 0, 0, 255))  # Red color
    stage.add_child(parent_actor)

    # Create a child actor
    child_actor = clutter.Actor.new()
    child_actor.set_color(clutter.Color(0, 0, 255, 255))  # Blue color
    stage.add_child(child_actor)

    # Create a BindConstraint to keep the child actor at 50% of the parent's width
    constraint = clutter.BindConstraint.new(
        parent_actor,                               # Source actor (parent)
        clutter.BindConstraintDimension.WIDTH,     # Dimension to bind to
        0.5                                          # Proportional size (50%)
    )

    # Add the constraint to the child actor
    child_actor.add_constraint(constraint)

    # Initial size update
    child_actor.set_size(0, 0)  # Will be updated by constraint

    # Show the stage
    stage.show_all()
    stage.connect('destroy', clutter.main_quit)

    # Start the main loop
    clutter.main()

if __name__ == "__main__":
    main()
