
import clutter

def main():
    # Initialize Clutter
    stage = clutter.Stage()
    stage.set_size(400, 400)
    stage.set_title("BindConstraint Example")

    # Create parent actor
    parent_actor = clutter.Actor()
    parent_actor.set_size(300, 200)
    parent_actor.set_position(50, 50)
    parent_actor.set_background_color(clutter.Color(0, 0, 255, 255))  # Blue
    stage.add_actor(parent_actor)

    # Create child actor
    child_actor = clutter.Actor()
    child_actor.set_size(150, 100)  # Initial size (not used)
    child_actor.set_position(30, 30)
    child_actor.set_background_color(clutter.Color(255, 0, 0, 255))  # Red
    parent_actor.add_child(child_actor)

    # Create a constraint to bind the child's width to half of the parent's width
    bind_constraint = clutter.BindConstraint()
    bind_constraint.set_source(parent_actor)
    bind_constraint.set_target(child_actor)
    bind_constraint.set_target_property("width")
    bind_constraint.set_source_property("width")
    bind_constraint.set_factor(0.5)  # Set the factor to 0.5 for 1/2

    # Add the constraint to the child actor
    child_actor.add_constraint(bind_constraint)

    # Show the stage
    stage.show_all()
    clutter.main()

if __name__ == "__main__":
    main()
