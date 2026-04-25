
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        self.Bind(wx.EVT_SIZE, self.on_resize)  # Bind the resize event

        self.Show()

    def on_resize(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Set desired percentage sizes
        percent_width = 0.2  # 20% of current width
        percent_height = 0.2  # 20% of current height

        # Calculate new width and height
        new_width = int(width * percent_width)
        new_height = int(height * percent_height)

        # Set the new size to the frame or panel
        self.SetSize(new_width, new_height)

if __name__ == '__main__':
    app = wx.App(False)
    Example(None, title='Size in Percentage')
    app.MainLoop()
