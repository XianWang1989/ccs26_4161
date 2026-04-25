
import clutter

def main():
    # Initialize the Clutter stage
    stage = clutter.Stage()
    stage.set_size(800, 600)
    stage.set_title("BindConstraint Example")

    # Create the parent actor
    parent = clutter.Actor()
    parent.set_size(400, 200)
    parent.set_position(200, 200)
    stage.add_child(parent)

    # Create the child actor
    child = clutter.Actor()
    child.set_size(200, 100)
    child.set_position(0, 0)
    parent.add_child(child)

    # Create a BindConstraint to keep the child's width half of the parent's width
    constraint = clutter.BindConstraint.create(
        child, 
        clutter.BindDimension.WIDTH, 
        parent, 
        clutter.BindDimension.WIDTH, 
        0.5  # Set the factor to 0.5 for half the width
    )

    # Add the constraint to the child actor
    child.add_constraint(constraint)

    # Show the stage
    stage.show_all()
    stage.connect("destroy", clutter.main_quit)
    clutter.main()

if __name__ == "__main__":
    main()
