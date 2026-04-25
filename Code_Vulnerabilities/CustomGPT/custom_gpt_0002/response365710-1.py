
Builder.load_string("""
#:import ListItemButton kivy.uix.listview.ListItemButton
#:import ListAdapter kivy.adapters.listadapter.ListAdapter

<ListViewModal>:
    ListView:
        size_hint: .8, .8
        adapter:
            ListAdapter(
            data=[(title, cat_dict.SECTION_DICT[title]) for title in root.categories],
            args_converter=lambda row_index, rec: \
            {'text': rec[0], 'on_press': lambda instance: root.callback(rec[1]), 'size_hint_y': None, 'height': 25},
            cls=ListItemButton)
""")

class ListViewModal(ModalView):
    categories = sorted(cat_dict.SECTION_DICT)

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, abbreviation):
        print("Abbreviation: " + abbreviation)
