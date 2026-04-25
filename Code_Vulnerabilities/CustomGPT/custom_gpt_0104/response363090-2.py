
import re

def filter_entrance_registers(requests):
    regex_pattern = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

    entrance_registers = EntranceRegister.objects.all()  # Fetch all initially

    # Filter using regex in Python
    filtered_registers = [
        register for register in entrance_registers
        if re.search(regex_pattern, register.authorized_requests)
    ]

    return filtered_registers
