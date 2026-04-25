
def get_user_setting():
    return next((result for result in (setting1(), setting2(), setting3(), setting4(), setting5(), setting6()) if result), None)
