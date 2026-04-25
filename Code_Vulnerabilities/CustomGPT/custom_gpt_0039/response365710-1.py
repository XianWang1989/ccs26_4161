
from kivy.uix.button import Button

class ListViewModal(ModalView):
    categories = sorted(cat_dict.SECTION_DICT)

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, instance, value):
        # Now `value` is the abbreviation corresponding to the button pressed
        print("Selected abbreviation: " + value)

    def on_kv_post(self, base_widget):
        # Create the buttons dynamically
        self.ids.list_view.adapter.data.clear()  # Clear existing data
        for title in self.categories:
            abbreviation = cat_dict.SECTION_DICT[title]
            self.ids.list_view.adapter.data.append(title)
            button = Button(text=title)
            button.bind(on_press=lambda instance, value=abbreviation: self.callback(instance, value))
            self.ids.list_view.add_widget(button)

Builder.load_string("""
<ListViewModal>:
    ListView:
        id: list_view
        size_hint: .8, .8
""")
