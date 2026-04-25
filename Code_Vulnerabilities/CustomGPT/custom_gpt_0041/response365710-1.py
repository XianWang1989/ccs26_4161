
adapter:
    ListAdapter(
    data=[(title, cat_dict.SECTION_DICT[title]) for title in root.categories],
    args_converter=lambda row_index, rec: \
    {'text': rec[0], 'on_press': lambda instance, abbr=rec[1]: root.callback(instance, abbr), 'size_hint_y': None, 'height': 25},
    cls=ListItemButton)
