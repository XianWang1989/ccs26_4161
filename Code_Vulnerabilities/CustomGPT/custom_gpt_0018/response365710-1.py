
# Modify the args_converter in your ListView load string
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
            {'text': rec,
             'on_press': lambda instance, abbrev=cat_dict.SECTION_DICT[rec]: root.callback(instance, abbrev),
             'size_hint_y': None,
             'height': 25},
            cls=ListItemButton)
""")

# Modify the callback method in ListViewModal
class ListViewModal(ModalView):
    categories = sorted(cat_dict.SECTION_DICT)

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, instance, abbreviation):
        print("Button clicked! Abbreviation: " + abbreviation)
