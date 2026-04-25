
import clutter

def create_actors():
    # Initialize Clutter
    stage = clutter.Stage()
    stage.set_size(400, 400)

    # Create parent actor
    parent_actor = clutter.Actor()
    parent_actor.set_size(300, 300)
    parent_actor.set_position(50, 50)
    stage.add_child(parent_actor)

    # Create child actor
    child_actor = clutter.Actor()
    child_actor.set_size(150, 150)  # Initial size
    child_actor.set_position(10, 10)  # Position relative to parent
    parent_actor.add_child(child_actor)

    # BindConstraint to make child width half of parent width
    bind_constraint = clutter.BindConstraint(child_actor, 
                                              clutter.BindConstraintType.WIDTH, 
                                              parent_actor, 
                                              clutter.BindConstraintType.WIDTH, 
                                              0.5)  # 50% of parent's width

    child_actor.add_constraint(bind_constraint)

    # Show the stage
    stage.show()

    # Start the Clutter main loop
    clutter.main()

if __name__ == "__main__":
    create_actors()
