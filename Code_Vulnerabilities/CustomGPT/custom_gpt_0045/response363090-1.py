
REQUEST_TYPE_ENTRANCE = 1

# Construct a like pattern for entrance requests.
LIKE_QUERY = '%{0}%'.format(REQUEST_TYPE_ENTRANCE)

# Query using LIKE instead of REGEXP
entrance_registers = EntranceRegister.objects.filter(authorized_requests__contains=str(REQUEST_TYPE_ENTRANCE))
