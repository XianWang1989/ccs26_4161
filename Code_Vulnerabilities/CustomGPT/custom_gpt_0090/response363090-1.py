
REQUEST_TYPE_ENTRANCE = 1
ENTRANCE_STR = str(REQUEST_TYPE_ENTRANCE)

entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__icontains=f',{ENTRANCE_STR},') | 
    EntranceRegister.objects.filter(authorized_requests__startswith=f'{ENTRANCE_STR},') | 
    EntranceRegister.objects.filter(authorized_requests__endswith(f',{ENTRANCE_STR}')) | 
    EntranceRegister.objects.filter(authorized_requests=ENTRANCE_STR)
