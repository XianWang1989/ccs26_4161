
REQUEST_TYPE_ENTRANCE = 1
entrant_str = str(REQUEST_TYPE_ENTRANCE)

entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__icontains=f',{entrant_str},') | 
    EntranceRegister.objects.filter(authorized_requests__startswith=f'{entrant_str},') | 
    EntranceRegister.objects.filter(authorized_requests__endswith=f',{entrant_str}') | 
    EntranceRegister.objects.filter(authorized_requests=entrant_str)
)
