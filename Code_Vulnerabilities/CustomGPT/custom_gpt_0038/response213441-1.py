
import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(400, 300))

        # Bind the size event to resize the content dynamically
        self.Bind(wx.EVT_SIZE, self.on_resize)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.Show()

    def on_resize(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate new size based on percentages
        new_width = int(width * 0.2)  # 20% of width
        new_height = int(height * 0.2)  # 20% of height

        # Create a new button with the calculated size
        button = wx.Button(self.panel, label='Click Me', size=(new_width, new_height))

        # Center the button
        button.Center()

        # Refresh the panel
        self.panel.Layout()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size Example')
    app.MainLoop()
