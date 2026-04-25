
# Call this to create the function at the start
create_regex_function()

# Now use it in your query
entrance_registers = EntranceRegister.objects.filter(
    Q(authorized_requests__regex=REGEX_ENTRANCE)
)
