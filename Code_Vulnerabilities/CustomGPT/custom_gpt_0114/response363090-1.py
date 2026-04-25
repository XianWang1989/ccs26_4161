
REQUEST_TYPE_ENTRANCE = 1
LIKE_PATTERN = '%{0}%'.format(REQUEST_TYPE_ENTRANCE)

entrance_registers = EntranceRegister.objects.filter(authorized_requests__icontains=LIKE_PATTERN)
