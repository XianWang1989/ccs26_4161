
class ListViewModal(ModalView):
    categories = sorted(cat_dict.SECTION_DICT.keys())

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, instance, abbreviation):
        print("Abbreviation:", abbreviation)

    def on_open(self):
        # Iterate through categories and create buttons
        for title in self.categories:
            abbreviation = cat_dict.SECTION_DICT[title]
            button = ListItemButton(text=title)
            button.bind(on_press=lambda instance, ab=abbreviation: self.callback(instance, ab))
            self.ids.your_list_view_id.add_widget(button)  # Make sure to replace this with your actual ListView ID
