
Builder.load_string("""
<ListViewModal>:
    ListView:
        size_hint: .8, .8
        adapter:
            ListAdapter(
            data=[i for i in root.categories],
            args_converter=lambda row_index, rec: \
            {'text': rec, 'on_press': lambda instance: root.callback(rec), 'size_hint_y': None, 'height': 25},
            cls=ListItemButton)

""")

class ListViewModal(ModalView):
    categories = sorted(cat_dict.SECTION_DICT)

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, title):
        abbreviation = cat_dict.SECTION_DICT[title]  # Get the abbreviation from the dictionary
        print("Abbreviation:", abbreviation)

# Rest of your code remains the same...

if __name__ == '__main__':
    CARApp().run()
