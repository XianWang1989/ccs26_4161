
def runFromChildToParent(self, child, textToSet):
    for child_widget in self.get_children():
        if child_widget.get_name() == child.get_name():
            print("Updating text on the child label.")
            child_widget.set_text(textToSet)
            child_widget.queue_draw()
