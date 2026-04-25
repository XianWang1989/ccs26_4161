
import clutter

def main():
    # Initialize Clutter
    clutter.init()

    # Create a stage
    stage = clutter.Stage.new()
    stage.set_size(800, 600)
    stage.set_title("Clutter BindConstraint Example")

    # Create parent actor
    parent_actor = clutter.Actor.new()
    parent_actor.set_size(400, 300)
    parent_actor.set_position(200, 150)
    parent_actor.set_background_color(clutter.Color(0, 0, 255, 255))  # Blue background
    stage.add_child(parent_actor)

    # Create child actor
    child_actor = clutter.Actor.new()
    child_actor.set_size(200, 150)  # Initial size (will be constrained)
    child_actor.set_position(0, 0)
    child_actor.set_background_color(clutter.Color(255, 0, 0, 255))  # Red background
    parent_actor.add_child(child_actor)

    # Create and apply BindConstraint to maintain half the parent's width
    bind_constraint = clutter.BindConstraint.new(child_actor, 
                                                  clutter.BindConstraintType.WIDTH, 
                                                  clutter.BindConstraintType.WIDTH, 
                                                  0.5)  # 50% of the parent's width
    child_actor.add_constraint(bind_constraint)

    # Show the stage
    stage.show_all()
    clutter.main()

if __name__ == "__main__":
    main()
