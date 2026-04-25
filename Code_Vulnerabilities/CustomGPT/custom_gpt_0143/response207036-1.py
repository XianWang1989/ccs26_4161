
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter

def update_size(actor, parent):
    parent_width = parent.get_width()
    new_width = parent_width / 2
    actor.set_size(new_width, actor.get_height())

def main():
    Clutter.init([])

    # Create the stage and parent actor
    stage = Clutter.Stage.new()
    stage.set_size(800, 600)

    parent_actor = Clutter.Actor.new()
    parent_actor.set_size(400, 300)
    parent_actor.set_position(200, 150)
    stage.add_child(parent_actor)

    # Create the child actor
    child_actor = Clutter.Actor.new()
    child_actor.set_size(100, 100)  # Initial size
    child_actor.set_position(50, 50)
    parent_actor.add_child(child_actor)

    # Bind the size constraint
    parent_actor.connect("size-changed", update_size, child_actor)

    # Show the stage
    stage.show()
    Clutter.threads_init()
    Clutter.main()

if __name__ == "__main__":
    main()
