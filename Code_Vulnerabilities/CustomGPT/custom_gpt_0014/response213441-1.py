
import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        # Get the size of the frame
        self.Bind(wx.EVT_SIZE, self.OnResize)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("light blue")

        self.Show()

    def OnResize(self, event):
        # Get the new size of the frame
        width, height = self.GetSize()

        # Calculate 20% of the width and height
        new_width = int(width * 0.2)
        new_height = int(height * 0.2)

        # Resize the panel to 20% of the frame size
        self.panel.SetSize((new_width, new_height))
        self.panel.Center()  # Center the panel in the frame

        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
