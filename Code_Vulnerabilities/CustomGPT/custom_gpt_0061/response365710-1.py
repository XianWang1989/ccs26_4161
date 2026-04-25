
# Update args_converter in your Builder.load_string section
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
            {'text': rec, 'on_press': lambda x: root.callback(cat_dict.SECTION_DICT[rec]), 'size_hint_y': None, 'height': 25},
            cls=ListItemButton)
""")

# Update your callback function
class ListViewModal(ModalView):
    categories = sorted(cat_dict.SECTION_DICT)

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, abbreviation):
        print("Abbreviation: " + abbreviation)  # Now it prints the abbreviation
