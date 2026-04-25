python_library(name="app-lib",
               source=globs("*.py"))

python_binary(name="myapp",
              source="Hello_world.py",
              dependencies=[":app-lib"])
