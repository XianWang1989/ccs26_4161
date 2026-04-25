
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        self.Bind(wx.EVT_SIZE, self.on_resize)

        # Creating a panel to demonstrate resizing
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(255, 200, 200))

        self.Show()

    def on_resize(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate 20% of the current width and height
        new_width = int(width * 0.2)
        new_height = int(height * 0.2)

        # Set a new size for the panel
        self.panel.SetSize(new_width, new_height)

        # Refresh the panel to update the display
        self.panel.Refresh()


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size with Percentage')
    app.MainLoop()
