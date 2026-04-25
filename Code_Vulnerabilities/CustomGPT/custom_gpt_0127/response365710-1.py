
class ListViewModal(ModalView):
    categories = sorted(cat_dict.SECTION_DICT.keys())  # Get only the keys for button titles

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, instance, abbreviation):
        print("Abbreviation:", abbreviation)  # Print the abbreviation

    def on_adapter(self):
        # Override to inject abbreviations into the buttons
        for title in self.categories:
            abbreviation = cat_dict.SECTION_DICT[title]
            button = ListItemButton(text=title)
            button.bind(on_press=lambda instance, ab=abbreviation: self.callback(instance, ab))
            self.ids.listview.add_widget(button)  # or use your method to add buttons to the ListView

