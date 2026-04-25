
def filter_entrance_registers(request_type):
    like_pattern = f'%{request_type}%'  # Pattern to match
    entrance_registers = EntranceRegister.objects.filter(authorized_requests__contains=request_type)

    return entrance_registers
