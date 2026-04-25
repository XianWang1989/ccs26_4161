
REQUEST_TYPE_ENTRANCE = 1
pattern = f"%{REQUEST_TYPE_ENTRANCE}%"

entrance_registers = EntranceRegister.objects.filter(authorized_requests__icontains=pattern)
