
import clutter

def main():
    stage = clutter.Stage()
    stage.set_size(800, 600)
    stage.set_title("BindConstraint Example")

    parent = clutter.Actor()
    parent.set_size(400, 300)  # Set the size of the parent actor
    parent.set_position(200, 150)
    parent.set_background_color(clutter.Color(255, 0, 0, 255))  # Red background
    stage.add_child(parent)

    child = clutter.Actor()
    child.set_size(100, 100)  # Initial size of the child actor
    child.set_position(50, 50)
    child.set_background_color(clutter.Color(0, 0, 255, 255))  # Blue background
    parent.add_child(child)

    # Create a BindConstraint to bind child's width to 50% of parent's width
    bind_constraint = clutter.BindConstraint.new(clutter.BindConstraintTarget.SIZE, parent, clutter.BindConstraintAlignments.ABSOLUTE)
    bind_constraint.set_percent(0.5)  # Set the child width to 50% of parent's width
    child.add_constraint(bind_constraint)

    stage.show()
    clutter.main()

if __name__ == "__main__":
    main()
