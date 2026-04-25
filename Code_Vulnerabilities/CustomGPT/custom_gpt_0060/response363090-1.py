
REQUEST_TYPE_ENTRANCE = 1
like_condition = '%{0}%'.format(REQUEST_TYPE_ENTRANCE)
entrance_registers = EntranceRegister.objects.filter(authorized_requests__icontains=like_condition)
