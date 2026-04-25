
import clutter

def create_actor_with_bind_constraint():
    # Initialize the Clutter stage
    stage = clutter.Stage()
    stage.set_size(800, 600)
    stage.show()

    # Create the parent actor
    parent = clutter.Actor()
    parent.set_size(400, 300)
    parent.set_color(clutter.Color(0, 0, 255, 255))  # Blue color
    stage.add_child(parent)

    # Create the child actor
    child = clutter.Actor()
    child.set_color(clutter.Color(255, 0, 0, 255))  # Red color
    parent.add_child(child)

    # Create a BindConstraint to keep the child's width to 1/2 of the parent's width
    def constrain_size():
        parent_width = parent.get_width()
        new_width = int(parent_width / 2)
        child.set_size(new_width, child.get_height())

    # Connect the 'width-changed' signal of the parent to the custom function
    parent.connect('width-changed', lambda actor: constrain_size())

    # Initial call to set the correct size
    constrain_size()

    # Show actors
    parent.show()
    child.show()

    # Main loop
    clutter.main()

if __name__ == '__main__':
    create_actor_with_bind_constraint()
