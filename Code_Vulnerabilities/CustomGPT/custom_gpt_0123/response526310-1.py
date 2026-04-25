
def get_setting():
    settings_sources = [foo, bar, baz]
    return next((source() for source in settings_sources if source()), None)

result = get_setting()
