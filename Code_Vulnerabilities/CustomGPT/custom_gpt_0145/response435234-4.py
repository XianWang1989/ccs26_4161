
import os
import importlib

# Assuming `plugins` is a subdirectory with `__init__.py`
plugins_dir = 'plugins'
for filename in os.listdir(plugins_dir):
    if filename.endswith('.py') and filename != '__init__.py':
        module_name = filename[:-3]  # Remove the .py extension
        importlib.import_module(f'{plugins_dir}.{module_name}')

manager = Manager()

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
