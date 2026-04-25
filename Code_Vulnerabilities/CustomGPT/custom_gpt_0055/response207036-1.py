
import clutter

def main():
    # Initialize Clutter
    clutter.init()

    # Create a stage
    stage = clutter.Stage()
    stage.set_size(800, 600)

    # Create a parent actor
    parent_actor = clutter.Actor()
    parent_actor.set_size(400, 200)
    parent_actor.set_position(200, 200)
    stage.add_child(parent_actor)

    # Create a child actor
    child_actor = clutter.Actor()
    child_actor.set_size(200, 100)  # Set an initial size
    child_actor.set_position(0, 0)
    parent_actor.add_child(child_actor)

    # Create a BindConstraint to constrain child's width to half of parent's width
    def resize_actor(child, parent):
        parent_width = parent.get_width()
        new_width = parent_width / 2
        child.set_size(new_width, child.get_height())

    # Connect the resize function to the parent's "size-changed" signal
    parent_actor.connect("size-changed", lambda actor: resize_actor(child_actor, actor))

    # Show the stage
    stage.show_all()

    # Start the Clutter main loop
    clutter.main()

if __name__ == "__main__":
    main()
