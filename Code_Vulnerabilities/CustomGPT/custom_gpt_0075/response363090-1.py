
entrance_registers = EntranceRegister.objects.all()
filtered_registers = [
    register for register in entrance_registers
    if re.match(REGEX_ENTRANCE, register.authorized_requests)
]
