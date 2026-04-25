
settings_funcs = [foo, bar, baz]  # Add more functions as needed

setting = next((value for func in settings_funcs if (value := func())), None)
