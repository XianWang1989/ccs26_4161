
def get_user_setting():
    return next((setting for setting in (user_specific_setting(), account_wide_setting(), default_setting()) if setting), None)
