
import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(400, 300))

        # Bind to size event to update layout
        self.Bind(wx.EVT_SIZE, self.on_size)

        # Create a panel
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))  # White background

        self.Show()

    def on_size(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate sizes as percentages
        new_width = int(width * 0.2)  # 20% of current width
        new_height = int(height * 0.2)  # 20% of current height

        # Resize the panel
        self.panel.SetSize((new_width, new_height))
        self.panel.Center()  # Center the panel

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
