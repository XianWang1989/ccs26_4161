
import clutter

def main():
    # Initialize Clutter
    stage = clutter.Stage.new()
    stage.set_size(800, 600)
    stage.set_title("BindConstraint Example")

    # Create the parent actor
    parent_actor = clutter.Actor.new()
    parent_actor.set_size(400, 200)  # Set parent size
    parent_actor.set_color(clutter.Color(255, 0, 0, 255))  # Red for visibility
    stage.add_child(parent_actor)

    # Create the child actor
    child_actor = clutter.Actor.new()
    child_actor.set_size(200, 100)  # Initial size
    child_actor.set_color(clutter.Color(0, 0, 255, 255))  # Blue for visibility
    stage.add_child(child_actor)

    # Create a BindConstraint for width
    width_constraint = clutter.BindConstraint.new(parent_actor, clutter.BindConstraintType.WIDTH, 0.5)
    child_actor.add_constraint(width_constraint)

    # Position the actors
    parent_actor.set_position(200, 250)
    child_actor.set_position(200, 250)

    # Show the stage
    stage.show_all()
    clutter.main()

if __name__ == "__main__":
    main()
