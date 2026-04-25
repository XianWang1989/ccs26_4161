
setting = next((value for func in (foo, bar, baz) if (value := func())), None)
