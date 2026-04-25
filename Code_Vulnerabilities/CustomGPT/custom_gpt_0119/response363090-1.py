
REQUEST_TYPE_ENTRANCE = 1
pattern = '%{},%'.format(REQUEST_TYPE_ENTRANCE)
entrance_registers = EntranceRegister.objects.filter(authorized_requests__icontains=str(REQUEST_TYPE_ENTRANCE))

# For exact matches at the start or end
entrance_registers = entrance_registers | EntranceRegister.objects.filter(authorized_requests__startswith=str(REQUEST_TYPE_ENTRANCE) + ',')
entrance_registers = entrance_registers | EntranceRegister.objects.filter(authorized_requests__endswith=',' + str(REQUEST_TYPE_ENTRANCE))

entrance_registers = entrance_registers.distinct()
