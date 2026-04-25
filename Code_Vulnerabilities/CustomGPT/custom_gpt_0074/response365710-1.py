
Builder.load_string("""
#:import ListItemButton kivy.uix.listview.ListItemButton
#:import ListAdapter kivy.adapters.listadapter.ListAdapter

<ListViewModal>:
    ListView:
        size_hint: .8, .8
        adapter:
            ListAdapter(
            data=[i for i in root.categories],
            # Modify args_converter to pass abbreviation and title
            args_converter=lambda row_index, rec: \
            {
                'text': rec,
                'on_press': lambda instance: root.callback(rec, cat_dict.SECTION_DICT[rec]),
                'size_hint_y': None,
                'height': 25
            },
            cls=ListItemButton)
""")
