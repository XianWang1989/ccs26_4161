
import clutter

def main():
    # Initialize Clutter
    stage = clutter.Stage()
    stage.set_size(800, 600)
    stage.set_title("BindConstraint Example")

    # Create a parent actor
    parent_actor = clutter.Actor()
    parent_actor.set_size(400, 300)
    parent_actor.set_position(200, 150)
    parent_actor.set_background_color(clutter.Color(255, 0, 0, 255))  # Red
    stage.add_child(parent_actor)

    # Create the child actor that size needs to be constrained
    child_actor = clutter.Actor()
    child_actor.set_size(1, 1)  # Initial size (this will be updated by the constraint)
    child_actor.set_background_color(clutter.Color(0, 0, 255, 255))  # Blue
    stage.add_child(child_actor)

    # Create a BindConstraint to bind the child's width to half of the parent's width
    bind_constraint = clutter.BindConstraint()
    bind_constraint.set_target(parent_actor)

    # Bind the width to half of the parent's width
    bind_constraint.set_property(clutter.BIND_CONSTRAINT_PROPERTY_WIDTH, 
                                 clutter.BIND_CONSTRAINT_BIND_SCALED, 0.5)

    # Add the constraint to the child actor
    child_actor.add_constraint(bind_constraint)

    # Show the stage
    stage.show_all()
    clutter.main()

if __name__ == "__main__":
    main()
