
import clutter

def create_constrained_actors():
    # Initialize Clutter
    stage = clutter.Stage()
    stage.set_size(800, 600)

    # Create parent actor
    parent = clutter.Actor()
    parent.set_size(400, 300)
    parent.set_position(200, 150)
    stage.add_child(parent)

    # Create child actor
    child = clutter.Actor()
    child.set_size(200, 150)  # Initial size (will be adjusted)
    child.set_position(0, 0)   # Position relative to parent
    parent.add_child(child)

    # Create BindConstraint to keep child's width to half of parent's width
    width_constraint = clutter.BindConstraint()
    width_constraint.set_property(clutter.BindConstraint.BOUND_PROPERTY_WIDTH)
    width_constraint.set_source(parent)
    width_constraint.set_ratio(0.5)  # Set ratio to 0.5 for 50%

    # Apply the constraint
    child.add_constraint(width_constraint)

    # Show the stage
    stage.show_all()
    stage.connect("destroy", clutter.main_quit)
    clutter.main()

if __name__ == "__main__":
    create_constrained_actors()
