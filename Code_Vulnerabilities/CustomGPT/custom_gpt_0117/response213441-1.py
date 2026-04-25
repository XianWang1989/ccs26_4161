
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Bind the Resize event to adjust layout size
        self.Bind(wx.EVT_SIZE, self.on_resize)

        # Create a panel to hold the controls
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.Show()

    def on_resize(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate new sizes based on percentage
        panel_width = int(width * 0.2)  # 20% of width
        panel_height = int(height * 0.2)  # 20% of height

        # Resize the panel
        self.panel.SetSize(panel_width, panel_height)
        self.panel.Centre()
        self.Layout()

if __name__ == '__main__':
    app = wx.App(False)
    Example(None, title='Size Example')
    app.MainLoop()
