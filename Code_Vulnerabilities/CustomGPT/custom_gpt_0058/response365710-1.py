
Builder.load_string("""
#:import ListItemButton kivy.uix.listview.ListItemButton
#:import ListAdapter kivy.adapters.listadapter.ListAdapter

<ListViewModal>:
    ListView:
        size_hint: .8, .8
        adapter:
            ListAdapter(
            data=[(title, abbrev) for title, abbrev in root.categories.items()],
            args_converter=lambda row_index, rec: \
            {'text': rec[0], 'on_press': lambda x: root.callback(rec[1]), 'size_hint_y': None, 'height': 25},
            cls=ListItemButton)
""")

class ListViewModal(ModalView):
    categories = sorted(cat_dict.SECTION_DICT.items())  # Use items() to access both keys and values

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, abbreviation):
        print("Abbreviation:", abbreviation)  # This will print the abbreviation of the clicked button
