
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, Gdk

def main():
    # Initialize Clutter
    Clutter.init([])

    # Create the stage
    stage = Clutter.Stage.new()
    stage.set_size(800, 600)
    stage.set_title("BindConstraint Example")
    stage.show()

    # Create parent actor
    parent_actor = Clutter.Actor.new()
    parent_actor.set_size(400, 300)
    parent_actor.set_position(200, 150)
    parent_actor.set_background_color(Clutter.Color.from_string("blue"))
    stage.add_child(parent_actor)

    # Create child actor
    child_actor = Clutter.Actor.new()
    child_actor.set_size(200, 150)  # Initial size
    child_actor.set_position(50, 50)
    child_actor.set_background_color(Clutter.Color.from_string("red"))
    parent_actor.add_child(child_actor)

    # Create a BindConstraint to bind the child's width to half of the parent's width
    bind_constraint = Clutter.BindConstraint.new(parent_actor, Clutter.BindFlags.SIZE)
    bind_constraint.set_target_dimension(Clutter.BindDimension.WIDTH)
    bind_constraint.set_target_value(0.5)  # 50% of the parent's width

    # Add the bind constraint to the child actor
    child_actor.add_constraint(bind_constraint)

    # Show all actors
    stage.show_all()

    # Start the main loop
    Clutter.mainloop()

if __name__ == "__main__":
    main()
