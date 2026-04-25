
REQUEST_TYPE_ENTRANCE = 1

# Define the pattern for matching
pattern = f'%{REQUEST_TYPE_ENTRANCE}%'

# Use Django's filter with LIKE instead of regex
entrance_registers = EntranceRegister.objects.filter(authorized_requests__icontains=REQUEST_TYPE_ENTRANCE)

# Alternatively, if you need to ensure strict matching with commas
entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__regex=f'^{REQUEST_TYPE_ENTRANCE}$|,{REQUEST_TYPE_ENTRANCE},|^{REQUEST_TYPE_ENTRANCE},|,{REQUEST_TYPE_ENTRANCE}$'
).extra(
    where=["authorized_requests GLOB ?"],
    params=[f"*{REQUEST_TYPE_ENTRANCE}*"]
)
