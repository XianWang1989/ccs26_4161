
Builder.load_string("""
<ListViewModal>:
    ListView:
        size_hint: .8, .8
        adapter:
            ListAdapter(
            data=[(title, abbr) for title, abbr in root.categories.items()],
            args_converter=lambda row_index, rec: \
            {'text': rec[0], 'on_press': lambda instance: root.callback(rec[1]), 'size_hint_y': None, 'height': 25},
            cls=ListItemButton)
""")

class ListViewModal(ModalView):
    categories = sorted(cat_dict.SECTION_DICT.items())  # Use items() for title-abbreviation pairs.

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, abbreviation):
        print("Abbreviation:", abbreviation)

# MainView and other classes remain the same.
