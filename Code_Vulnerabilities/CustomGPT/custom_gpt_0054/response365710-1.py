
class ListViewModal(ModalView):
    categories = sorted(cat_dict.SECTION_DICT)

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, abbreviation):
        print("Selected abbreviation:", abbreviation)

    def get_abbreviation(self, category):
        return cat_dict.SECTION_DICT.get(category, "")

Builder.load_string("""
#:import ListItemButton kivy.uix.listview.ListItemButton
#:import ListAdapter kivy.adapters.listadapter.ListAdapter

<ListViewModal>:
    ListView:
        size_hint: .8, .8
        adapter:
            ListAdapter(
            data=[i for i in root.categories],
            args_converter=lambda row_index, rec: \
            {'text': rec, 'on_press': lambda instance: root.callback(root.get_abbreviation(rec)), 'size_hint_y': None, 'height': 25},
            cls=ListItemButton)
""")
