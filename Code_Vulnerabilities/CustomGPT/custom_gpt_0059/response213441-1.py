
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Bind to the size event to get the frame size
        self.Bind(wx.EVT_SIZE, self.on_size)

        # Initial size set to 20% of default dimensions
        self.SetInitialSize()

        self.Show()

    def SetInitialSize(self):
        # Get the current screen size
        screen_size = wx.GetDisplaySize()

        # Calculate dimensions based on percentage (20%)
        width = int(screen_size[0] * 0.2)
        height = int(screen_size[1] * 0.2)

        # Set the size of the frame
        self.SetSize((width, height))

    def on_size(self, event):
        # Get the current size of the frame
        size = self.GetSize()

        print(f"Current size: {size}")
        event.Skip()  # Allow other handlers to process the event

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
