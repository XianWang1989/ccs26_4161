
def main():
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    win.start_update()  # Start the update loop
    Gtk.main()

if __name__ == "__main__":
    main()
