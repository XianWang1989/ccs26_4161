
import clutter

def main():
    # Initialize Clutter
    clutter.init([])

    # Create a stage
    stage = clutter.Stage.new()
    stage.set_size(800, 600)

    # Create the parent actor
    parent = clutter.Actor()
    parent.set_size(400, 300)
    parent.set_position(200, 150)
    parent.set_background_color(clutter.Color.from_string("blue"))
    stage.add_child(parent)

    # Create the child actor
    child = clutter.Actor()
    child.set_background_color(clutter.Color.from_string("red"))

    # Add the child to the parent
    parent.add_child(child)

    # Create a BindConstraint to bind the size of the child actor
    bind_constraint = clutter.BindConstraint(parent, clutter.BindChildren.width)
    child.add_constraint(bind_constraint)

    # Set proportional size (1/2 the width of the parent)
    bind_constraint.set_target(parent, 0.5)

    # Show everything
    stage.show_all()
    stage.connect("destroy", clutter.main_quit)
    clutter.main()

if __name__ == "__main__":
    main()
