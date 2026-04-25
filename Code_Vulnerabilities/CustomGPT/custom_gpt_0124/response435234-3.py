
def load_plugins():
    plugin_files = glob.glob(os.path.join('plugins', '*.py'))
    for plugin_file in plugin_files:
        # Import each plugin module
        module_name = os.path.basename(plugin_file)[:-3]  # Remove .py extension
        __import__(f'plugins.{module_name}')

if __name__ == "__main__":
    load_plugins()  # Load and register all plugins
    main()
