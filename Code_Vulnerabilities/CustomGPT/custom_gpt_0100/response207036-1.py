
import clutter

def main():
    # Initialize Clutter
    clutter.init()

    # Create a stage
    stage = clutter.Stage.new()
    stage.set_size(800, 600)
    stage.show()

    # Create parent actor
    parent = clutter.Actor.new()
    parent.set_size(400, 300)
    parent.set_background_color(clutter.Color.new(255, 0, 0, 255))  # Red
    stage.add_child(parent)

    # Create child actor
    child = clutter.Actor.new()
    child.set_size(200, 150)
    child.set_background_color(clutter.Color.new(0, 0, 255, 255))  # Blue
    parent.add_child(child)

    # Create bind constraint for width
    # This sets the child's width to be 50% of the parent's width
    bind_constraint = clutter.BindConstraint.new(child, clutter.BindConstraintFlags.WIDTH, parent)
    bind_constraint.set_source_value(parent.get_width() / 2)
    child.add_constraint(bind_constraint)

    # Show the actors
    stage.show_all()

    # Start the main loop
    clutter.main()

if __name__ == '__main__':
    main()
