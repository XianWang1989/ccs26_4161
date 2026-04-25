
# application.py
manager = Manager()

# Import each plugin to trigger registration
import plugins.plugin1
import plugins.plugin2
import plugins.example_plugin
import plugins.plugin3.player  # If that plugin has registration

def main():
    print(manager.plugins)

if __name__ == "__main__":
    main()
