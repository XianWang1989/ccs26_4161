
entrance_registers = EntranceRegister.objects.raw('SELECT * FROM porter_entranceregister WHERE authorized_requests REGEXP ?', [REGEX_ENTRANCE])
