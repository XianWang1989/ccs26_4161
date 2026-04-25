import gi
gi.require_version('Clutter', '1.0')
from gi.repository import Clutter, GObject

Clutter.init([])

def on_parent_allocate(parent, allocation, child):
    width = allocation.width
    height = allocation.height
    # Set child width to 1/2 of parent's width, keep the height same or set as needed
    child.set_size(width // 2, height)

stage = Clutter.Stage()
stage.set_title("BindConstraint Example")
stage.set_user_resizable(True)
stage.set_size(600, 400)
stage.connect("destroy", Clutter.main_quit)

parent_actor = Clutter.Actor()
parent_actor.set_background_color(Clutter.Color.new(0, 255, 0, 255))
parent_actor.set_size(600, 400)
stage.add_child(parent_actor)

child_actor = Clutter.Actor()
child_actor.set_background_color(Clutter.Color.new(255, 0, 0, 255))
parent_actor.add_child(child_actor)

# Connect to the parent actor's allocate signal
parent_actor.connect("allocate", on_parent_allocate, child_actor)

stage.show_all()
Clutter.main()
