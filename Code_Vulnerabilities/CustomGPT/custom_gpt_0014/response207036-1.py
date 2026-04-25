
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, Gtk

def main():
    Clutter.init([])

    stage = Clutter.Stage.new()
    stage.set_size(800, 600)
    stage.show()

    # Create a parent actor
    parent = Clutter.Actor()
    parent.set_size(400, 300)
    parent.set_position(200, 150)
    stage.add_child(parent)

    # Create a child actor
    child = Clutter.Actor()
    child.set_color(Clutter.Color.from_string("blue"))
    child.set_size(0, 100)  # Initial width is 0, height is 100
    child.set_position(0, 100)
    parent.add_child(child)

    # Create a BindConstraint to link child's width to half of parent's width
    bind_constraint = Clutter.BindConstraint.new(parent, Clutter.BindFlags.WIDTH, 0.5)
    child.add_constraint(bind_constraint)

    # Show actors
    parent.show()
    child.show()

    Clutter.main()

if __name__ == '__main__':
    main()
