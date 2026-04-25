
import clutter

def create_child_actor(parent_actor):
    # Create a new child actor
    child_actor = clutter.Actor()
    child_actor.set_background_color(clutter.Color(255, 0, 0, 255)) # Red for visibility

    # Create the BindConstraint for proportional resizing (1/2 of parent)
    def resize_child_actor():
        parent_width = parent_actor.get_width()
        parent_height = parent_actor.get_height()
        new_width = parent_width / 2
        new_height = parent_height / 2

        # Set the new size to the child actor
        child_actor.set_size(new_width, new_height)

    # Connect the "notify::size" property of the parent actor to the resize function
    parent_actor.connect("notify::size", lambda *_: resize_child_actor())

    # Set initial size
    resize_child_actor()

    return child_actor

def main():
    # Initialize Clutter
    clutter.init([])

    # Create a stage
    stage = clutter.Stage()
    stage.set_size(800, 600)
    stage.set_title("BindConstraint Example")
    stage.show()

    # Create parent actor
    parent_actor = clutter.Actor()
    parent_actor.set_size(400, 300)
    parent_actor.set_background_color(clutter.Color(0, 255, 0, 255)) # Green for visibility
    stage.add_child(parent_actor)

    # Create and add child actor to the parent
    child_actor = create_child_actor(parent_actor)
    parent_actor.add_child(child_actor)

    # Show actors
    parent_actor.show()
    child_actor.show()

    # Start the main loop
    clutter.main()

if __name__ == "__main__":
    main()
