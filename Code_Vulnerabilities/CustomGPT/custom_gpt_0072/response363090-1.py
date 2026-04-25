
REQUEST_TYPE_ENTRANCE = 1
request_pattern = str(REQUEST_TYPE_ENTRANCE)

# Modify the regex query to use `LIKE`
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__icontains=request_pattern
)
