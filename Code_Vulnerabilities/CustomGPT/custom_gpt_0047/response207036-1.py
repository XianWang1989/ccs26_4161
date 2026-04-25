
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

class Example:
    def __init__(self):
        Clutter.init()
        self.stage = Clutter.Stage()
        self.stage.set_size(800, 600)
        self.stage.set_title("BindConstraint Example")
        self.stage.set_color(Clutter.Color.new(255, 255, 255, 255))

        # Create the parent actor
        self.parent_actor = Clutter.Actor()
        self.parent_actor.set_size(400, 200)
        self.parent_actor.set_color(Clutter.Color.new(0, 100, 200, 255))
        self.stage.add_child(self.parent_actor)

        # Create the child actor
        self.child_actor = Clutter.Actor()
        self.child_actor.set_size(200, 200)
        self.child_actor.set_color(Clutter.Color.new(255, 0, 0, 255))
        self.stage.add_child(self.child_actor)

        # Bind the width of the child actor to half of the parent's width
        self.child_actor.add_constraint(Clutter.BindConstraint.new(self.parent_actor,
            Clutter.BindDimension.WIDTH, Clutter.BindDimension.WIDTH, 0.5))

        self.parent_actor.set_position(200, 200)
        self.child_actor.set_position(200, 200)

        self.stage.show_all()
        Clutter.main()

if __name__ == "__main__":
    Example()
