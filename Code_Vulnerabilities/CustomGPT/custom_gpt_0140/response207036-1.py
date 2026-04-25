
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject, Gio

class Example:
    def __init__(self):
        Clutter.init([])

        # Create a stage
        self.stage = Clutter.Stage.new()
        self.stage.set_title("BindConstraint Example")
        self.stage.set_size(400, 400)
        self.stage.show()

        # Create a parent actor
        self.parent = Clutter.Actor.new()
        self.parent.set_size(400, 200)
        self.parent.set_position(0, 100)
        self.parent.set_bg_color(Clutter.Color.from_string("lightblue"))
        self.stage.add_child(self.parent)

        # Create the child actor
        self.child = Clutter.Actor.new()
        self.child.set_size(200, 100)
        self.child.set_position(0, 50)
        self.child.set_bg_color(Clutter.Color.from_string("orange"))
        self.parent.add_child(self.child)

        # Create a bind constraint to keep the child at half the width of the parent
        self.bind_width_constraint()

        Clutter.main()

    def bind_width_constraint(self):
        # Create a new BindConstraint
        constraint = Clutter.BindConstraint.new(self.parent, 
                                                 Clutter.BindFlags.WIDTH, 
                                                 0.5)  # 50% of the parent width

        # Add the constraint to the child actor
        self.child.add_constraint(constraint)

if __name__ == "__main__":
    Example()
