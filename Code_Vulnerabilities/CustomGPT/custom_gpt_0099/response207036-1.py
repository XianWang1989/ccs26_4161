
import gi
gi.require_version("Clutter", "1.0")
from gi.repository import Clutter, Gtk

def main():
    Clutter.init([])

    # Create a stage
    stage = Clutter.Stage.new()
    stage.set_size(800, 600)
    stage.set_title("BindConstraint Example")

    # Create a parent actor
    parent = Clutter.Actor.new()
    parent.set_size(400, 200)
    parent.set_position(200, 200)
    parent.set_background_color(Clutter.Color.from_string("blue"))

    # Create the child actor
    child = Clutter.Actor.new()
    child.set_size(200, 100)  # Initial size, will be constrained
    child.set_position(0, 0)
    child.set_background_color(Clutter.Color.from_string("red"))

    # Add actors to the stage
    stage.add_child(parent)
    parent.add_child(child)

    # Create a BindConstraint to make the child's width half of the parent's width
    bind_constraint = Clutter.BindConstraint.new(child, 
                                                  parent,
                                                  Clutter.BindFlags.WIDTH)
    bind_constraint.set_scale(0.5)  # Scale to half

    # Apply the constraint
    child.add_constraint(bind_constraint)

    # Show the stage
    stage.show_all()
    stage.connect("destroy", Gtk.main_quit)

    # Start the GTK main loop
    Gtk.main()

if __name__ == "__main__":
    main()
