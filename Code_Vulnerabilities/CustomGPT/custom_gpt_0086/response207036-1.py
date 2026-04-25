
import clutter

def create_actors():
    # Initialize Clutter
    stage = clutter.Stage()
    stage.set_size(800, 600)
    stage.set_title("BindConstraint Example")

    # Create parent actor
    parent_actor = clutter.Actor()
    parent_actor.set_size(400, 200)
    parent_actor.set_position(200, 200)
    stage.add_actor(parent_actor)

    # Create child actor
    child_actor = clutter.Actor()
    child_actor.set_size(200, 100)  # Starting size
    child_actor.set_position(0, 0)
    parent_actor.add_actor(child_actor)

    # Create a BindConstraint to constrain the child's width to half of the parent's width
    bind_constraint = clutter.BindConstraint()
    bind_constraint.set_target(parent_actor)
    bind_constraint.set_target_property("width")
    bind_constraint.set_source_property("width")
    bind_constraint.set_factor(0.5)  # Set the proportion to 1/2

    # Apply the constraint to the child actor
    child_actor.add_constraint(bind_constraint)

    # Show the stage
    stage.show_all()
    stage.connect("destroy", clutter.main_quit)
    clutter.main()

create_actors()
