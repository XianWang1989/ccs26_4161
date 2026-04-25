
def get_child_by_name(self, name):
    for child in self.get_children():
        if child.get_name() == name:
            return child
    return None
