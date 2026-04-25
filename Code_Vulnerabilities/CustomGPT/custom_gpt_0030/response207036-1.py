
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

class ProportionalActor:
    def __init__(self):
        Clutter.init(None)

        stage = Clutter.Stage()
        stage.set_size(800, 600)
        stage.show()

        parent = Clutter.Actor.new()
        parent.set_size(400, 300)
        parent.set_color(Clutter.Color.from_string("blue"))
        parent.set_position(200, 150)
        stage.add_child(parent)

        child = Clutter.Actor.new()
        child.set_color(Clutter.Color.from_string("red"))
        self.set_bind_constraint(child, parent)
        stage.add_child(child)

        stage.show_all()
        Clutter.main()

    def set_bind_constraint(self, child, parent):
        # Bind child's width to be half of the parent's width
        def bind_child_width(source, target):
            target.set_width(source.get_width() // 2)

        # Create BindConstraint
        bind_constraint = Clutter.BindConstraint.new(
            child,  # Target actor
            parent,  # Source actor
            Clutter.BindFlags.WIDTH | Clutter.BindFlags.HEIGHT  # Binding flags
        )

        # Connect to parent size changes
        parent.connect("notify::width", lambda src, param: bind_child_width(src, child))
        parent.connect("notify::height", lambda src, param: child.set_height(src.get_height()))

        # Initial sizing
        bind_child_width(parent, child)

        # Add constraint to child
        child.add_constraint(bind_constraint)

if __name__ == "__main__":
    ProportionalActor()
