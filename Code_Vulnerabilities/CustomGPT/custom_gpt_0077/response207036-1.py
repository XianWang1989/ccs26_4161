
import clutter

def create_actors():
    # Initialize the Clutter stage
    stage = clutter.Stage()
    stage.set_size(400, 400)

    # Create the parent actor
    parent_actor = clutter.Actor()
    parent_actor.set_size(200, 100)
    parent_actor.set_position(50, 150)
    parent_actor.set_background_color(clutter.Color(255, 0, 0, 255))
    stage.add_child(parent_actor)

    # Create the child actor
    child_actor = clutter.Actor()
    child_actor.set_size(100, 50)  # Initial size, will be constrained
    child_actor.set_position(100, 175)
    child_actor.set_background_color(clutter.Color(0, 0, 255, 255))
    stage.add_child(child_actor)

    # Create a bind constraint to set the child's width to half of the parent's width
    def bind_child_width_to_parent(child, parent):
        child_width = parent.get_width() / 2
        child.set_size(child_width, child.get_height())

    # Bind the child's size to the parent's size
    parent_actor.connect("size-changed", bind_child_width_to_parent, child_actor)

    # Show the stage
    stage.show_all()
    stage.loop()

create_actors()
