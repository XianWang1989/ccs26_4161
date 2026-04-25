
import clutter

def main():
    # Initialize Clutter
    stage = clutter.Stage()

    # Create the parent actor
    parent = clutter.Actor(width=400, height=300)
    parent.set_background_color(clutter.Color(0, 0, 255, 255))  # Blue background

    # Create the child actor
    child = clutter.Actor(width=200, height=150)
    child.set_background_color(clutter.Color(255, 0, 0, 255))  # Red background

    # Add actors to the stage
    stage.add_child(parent)
    parent.add_child(child)

    # Create a BindConstraint to bind the child's width to half of the parent's width
    bind_constraint = clutter.BindConstraint(child, clutter.BindConstraint.BIND_WIDTH, parent, clutter.BindConstraint.BIND_WIDTH, 0.5)
    child.add_constraint(bind_constraint)

    # Show the stage
    stage.set_size(800, 600)
    stage.show()

if __name__ == "__main__":
    main()
