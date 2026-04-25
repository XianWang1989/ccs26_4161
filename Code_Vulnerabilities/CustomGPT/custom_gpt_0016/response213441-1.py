
import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Set initial size of the frame
        self.SetSize((400, 300))  # Example size for the main frame

        # Set size in percentage (for example, 20% of width and height)
        self.percent_width = 20
        self.percent_height = 20

        # Create a panel and size it based on parent dimensions
        self.panel = wx.Panel(self)
        self.size_panel_in_percentage()

        self.Show()

    def size_panel_in_percentage(self):
        # Get current size of the frame
        width, height = self.GetSize()

        # Calculate size based on percentages
        panel_width = int(width * (self.percent_width / 100))
        panel_height = int(height * (self.percent_height / 100))

        # Set the panel size
        self.panel.SetSize((panel_width, panel_height))

if __name__ == '__main__':
    app = wx.App(False)
    Example(None, title='Size')
    app.MainLoop()
