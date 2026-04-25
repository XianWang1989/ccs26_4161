
Builder.load_string("""
#:import ListItemButton kivy.uix.listview.ListItemButton
#:import ListAdapter kivy.adapters.listadapter.ListAdapter


&lt;ListViewModal&gt;:
    ListView:
        size_hint: .8, .8
        adapter:
            ListAdapter(
            data=[(title, abbreviation) for title, abbreviation in root.categories.items()],
            args_converter=lambda row_index, rec: \
            {'text': rec[0], 'on_press': lambda instance: root.callback(instance, rec[1]), 'size_hint_y': None, 'height': 25},
            cls=ListItemButton)

""")

class ListViewModal(ModalView):
    categories = cat_dict.SECTION_DICT  # No need to sort since we're just using items directly

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, instance, abbreviation):
        print("Abbreviation: " + abbreviation)  # This will print the abbreviation when clicked


class MainView(GridLayout):

    def __init__(self, **kwargs):
        kwargs['cols'] = 1
        super(MainView, self).__init__(**kwargs)

        listview_modal = ListViewModal()
        self.add_widget(listview_modal)
