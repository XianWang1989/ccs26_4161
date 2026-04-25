
#!/usr/bin/env python

import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

# Initialize Clutter
Clutter.init([])

# Create the main stage
stage = Clutter.Stage.new()
stage.set_size(800, 600)
stage.set_title('BindConstraint Example')
stage.show()

# Create a parent actor
parent = Clutter.Actor.new()
parent.set_size(400, 200)
parent.set_color(Clutter.Color.new(0, 0, 255, 255))  # Blue color
stage.add_child(parent)

# Create a child actor
child = Clutter.Actor.new()
child.set_size(100, 100)
child.set_color(Clutter.Color.new(255, 0, 0, 255))  # Red color
parent.add_child(child)

# Create a BindConstraint to bind child's width to half of parent's width
def bind_width(child, parent):
    # Calculate half of parent's width
    desired_width = parent.get_width() / 2
    child.set_width(desired_width)

# Listen to the parent actor's size changes
parent.connect('notify::width', lambda source, param: bind_width(child, parent))

# Perform the initial binding
bind_width(child, parent)

# Show all actors
parent.show()
child.show()

# Start the main loop
Clutter.main()
