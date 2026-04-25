args_converter=lambda row_index, rec: {
    'text': rec,
    'on_press': lambda btn: root.callback(cat_dict.SECTION_DICT[rec]),
    'size_hint_y': None,
    'height': 25
}
