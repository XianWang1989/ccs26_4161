
import clutter

def main():
    # Initialize Clutter
    clutter.init()

    # Create a main stage
    stage = clutter.Stage()
    stage.set_size(800, 600)
    stage.set_title("BindConstraint Example")
    stage.show()

    # Create a parent actor
    parent_actor = clutter.Actor()
    parent_actor.set_size(400, 200)
    parent_actor.set_position(200, 200)
    parent_actor.set_background_color(clutter.Color(255, 0, 0, 255))  # Red
    stage.add_child(parent_actor)

    # Create a child actor
    child_actor = clutter.Actor()
    child_actor.set_size(200, 100)  # Initial size
    child_actor.set_position(0, 0)
    child_actor.set_background_color(clutter.Color(0, 0, 255, 255))  # Blue
    parent_actor.add_child(child_actor)

    # Create a BindConstraint to keep the child at 50% width of the parent
    constraint = clutter.BindConstraint()
    constraint.set_source(parent_actor)
    constraint.set_source_property("width")
    constraint.set_target_property("width")
    constraint.set_factor(0.5)  # Define the factor (50%)

    # Add the constraint to the child actor
    child_actor.add_constraint(constraint)

    # Start the Clutter main loop
    clutter.main()

if __name__ == "__main__":
    main()
