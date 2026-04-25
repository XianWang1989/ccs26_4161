
import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

def main():
    Clutter.init([])

    # Create a stage
    stage = Clutter.Stage.new()
    stage.set_size(800, 600)
    stage.set_title("BindConstraint Example")
    stage.show()

    # Create a parent actor
    parent_actor = Clutter.Actor.new()
    parent_actor.set_size(400, 300)
    parent_actor.set_position(200, 150)
    stage.add_child(parent_actor)

    # Create a child actor
    child_actor = Clutter.Actor.new()
    child_actor.set_size(200, 150)
    child_actor.set_position(0, 0)
    parent_actor.add_child(child_actor)

    # Create a BindConstraint to link the width of child_actor to half of parent_actor's width
    bind_constraint = Clutter.BindConstraint.new(child_actor, Clutter.BindConstraintSource.new(parent_actor, "width"))
    bind_constraint.set_scale(0.5)  # Scale the width to be half of the parent's width
    child_actor.add_constraint(bind_constraint)

    stage.show_all()
    Clutter.main()

if __name__ == "__main__":
    main()
