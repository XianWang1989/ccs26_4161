
REQUEST_TYPE_ENTRANCE = 1
like_pattern = '%{}%'.format(REQUEST_TYPE_ENTRANCE)
entrance_registers = EntranceRegister.objects.filter(authorized_requests__like=like_pattern)
