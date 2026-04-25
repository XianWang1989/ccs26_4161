
class ListViewModal(ModalView):
    categories = sorted(cat_dict.SECTION_DICT)

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    # Update the callback to receive both title and abbreviation
    def callback(self, instance, abbreviation):
        print("Title: {}, Abbreviation: {}".format(instance, abbreviation))
