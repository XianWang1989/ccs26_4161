
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

class MyApplication:
    def __init__(self):
        Clutter.init([])

        # Create the stage
        self.stage = Clutter.Actor.new()
        self.stage.set_size(800, 600)
        self.stage.show()

        # Create the parent actor
        self.parent = Clutter.Actor.new()
        self.parent.set_size(400, 300)
        self.parent.set_position(200, 150)
        self.parent.set_background_color(Clutter.Color.from_string("lightblue"))
        self.stage.add_actor(self.parent)

        # Create the child actor
        self.child = Clutter.Actor.new()
        self.child.set_size(200, 150)
        self.child.set_position(50, 50)
        self.child.set_background_color(Clutter.Color.from_string("lightgreen"))
        self.parent.add_actor(self.child)

        # Bind the child's width to be half of the parent's width
        self.bind_constraint()

        # Show all actors
        self.stage.show_all()

        Clutter.main()

    def bind_constraint(self):
        # Create a BindConstraint that binds the width of the child actor
        constraint = Clutter.BindConstraint.new(self.parent, Clutter.BindDimension.WIDTH)
        # Set the binding factor to 0.5 (half)
        constraint.set_scale(0.5)
        self.child.add_constraint(constraint)

if __name__ == "__main__":
    app = MyApplication()
