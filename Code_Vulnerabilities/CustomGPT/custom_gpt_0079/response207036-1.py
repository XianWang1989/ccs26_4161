
import clutter

def main():
    # Initialize the Clutter stage
    stage = clutter.Stage()
    stage.set_size(800, 600)
    stage.show()

    # Create parent actor
    parent_actor = clutter.Actor()
    parent_actor.set_size(400, 200)
    parent_actor.set_position(200, 200)
    stage.add_child(parent_actor)

    # Create child actor
    child_actor = clutter.Actor()
    child_actor.set_size(0, 200)  # Initial width of 0 (it will be bound)
    child_actor.set_position(0, 0)
    parent_actor.add_child(child_actor)

    # BindConstraint to set child width to half the parent's width
    def on_parent_size_changed(actor, constraint):
        parent_width = actor.get_width()
        child_actor.set_size(parent_width / 2, 200)

    # Connect the signal for size changes
    parent_actor.connect("notify::allocation", on_parent_size_changed)

    # Show the actors
    parent_actor.show()
    child_actor.show()

    # Run the Clutter main loop
    clutter.main()

if __name__ == '__main__':
    main()
