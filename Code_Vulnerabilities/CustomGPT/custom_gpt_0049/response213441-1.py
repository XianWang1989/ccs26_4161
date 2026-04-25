
import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Bind the 'size' event to handle resizing.
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Show()

    def on_size(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate new size based on percentages
        new_width = int(width * 0.20)  # 20%
        new_height = int(height * 0.20)  # 20%

        # Set the size of the frame
        self.SetSize(new_width, new_height)

        event.Skip()  # Allow further event processing

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
