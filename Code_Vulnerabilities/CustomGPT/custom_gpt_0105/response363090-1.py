
REQUEST_TYPE_ENTRANCE = 1
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__icontains=str(REQUEST_TYPE_ENTRANCE)  # This checks if the string contains the entrance request type.
)

# For more specific matching, you can adjust the filter like this:
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__exact=f"{REQUEST_TYPE_ENTRANCE}"  # Only matches the exact value.
) | EntranceRegister.objects.filter(
    authorized_requests__startswith=f"{REQUEST_TYPE_ENTRANCE},"  # Matches if it starts with the entrance request.
) | EntranceRegister.objects.filter(
    authorized_requests__endswith=f",{REQUEST_TYPE_ENTRANCE}"  # Matches if it ends with the entrance request.
)
