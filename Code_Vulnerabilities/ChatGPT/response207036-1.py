
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

class MyApp:
    def __init__(self):
        # Initialize Clutter
        Clutter.init(None)

        # Create a stage (the main container)
        self.stage = Clutter.Stage.new()
        self.stage.set_size(800, 600)
        self.stage.set_title("BindConstraint Example")
        self.stage.show()

        # Create a parent actor
        self.parent_actor = Clutter.Actor.new()
        self.parent_actor.set_size(400, 300)
        self.parent_actor.set_color(Clutter.Color.from_string("blue"))
        self.parent_actor.set_position(200, 150)
        self.stage.add_child(self.parent_actor)

        # Create a child actor that we want to bind
        self.child_actor = Clutter.Actor.new()
        self.child_actor.set_color(Clutter.Color.from_string("red"))
        self.child_actor.set_size(0, 0)  # Initially, we can set size to 0
        self.child_actor.set_position(50, 50)
        self.parent_actor.add_child(self.child_actor)

        # Create a bind constraint to link the child actor's width to half of the parent's width
        self.bind_constraint = Clutter.BindConstraint.new(self.child_actor, 
                                                           Clutter.BindFlags.X | Clutter.BindFlags.WIDTH, 
                                                           self.parent_actor, 
                                                           Clutter.BindFlags.X | Clutter.BindFlags.WIDTH)

        # Add the constraint to the child actor
        self.child_actor.add_constraint(self.bind_constraint)

        # Connect the "size-changed" signal to update the child's size proportionally
        self.parent_actor.connect("size-changed", self.update_child_size)

        # Show the actors
        self.parent_actor.show()

    def update_child_size(self, actor):
        # Calculate the new width for the child actor (half the parent's width)
        width = actor.get_width() // 2
        self.child_actor.set_size(width, self.child_actor.get_height())

if __name__ == "__main__":
    app = MyApp()
    Clutter.main()
