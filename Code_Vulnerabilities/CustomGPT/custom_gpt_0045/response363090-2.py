
# Matches: ',1,' or '1,' or ',1' or '1'
LIKE_QUERY = '%,{0},%'.format(REQUEST_TYPE_ENTRANCE)

# Perform filtering
entrance_registers = EntranceRegister.objects.filter(authorized_requests__contains=str(REQUEST_TYPE_ENTRANCE)) | EntranceRegister.objects.filter(authorized_requests__endswith=',' + str(REQUEST_TYPE_ENTRANCE)) | EntranceRegister.objects.filter(authorized_requests__startswith=str(REQUEST_TYPE_ENTRANCE) + ',') | EntranceRegister.objects.filter(authorized_requests=str(REQUEST_TYPE_ENTRANCE))
