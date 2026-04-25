
# Import statements remain the same

Builder.load_string("""
#:import ListItemButton kivy.uix.listview.ListItemButton
#:import ListAdapter kivy.adapters.listadapter.ListAdapter

<ListViewModal>:
    ListView:
        size_hint: .8, .8
        adapter:
            ListAdapter(
                data=root.categories,
                args_converter=lambda row_index, rec: \
                {'text': rec, 'on_press': lambda instance: root.callback(rec), 'size_hint_y': None, 'height': 25},
                cls=ListItemButton)
""")

class ListViewModal(ModalView):
    categories = list(cat_dict.SECTION_DICT.keys())  # Obtain the list of titles (keys)

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, title):
        abbreviation = cat_dict.SECTION_DICT[title]  # Retrieve abbreviation using title
        print("The abbreviation for '{}' is: {}".format(title, abbreviation))

# The rest of your classes remain unchanged

if __name__ == '__main__':
     CARApp().run()
