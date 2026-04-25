
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get the size of the screen
        screen_size = wx.GetDisplaySize()

        # Convert percentage to pixel size
        width = int(screen_size[0] * 0.2)  # 20% of screen width
        height = int(screen_size[1] * 0.2)  # 20% of screen height

        # Set the size of the frame
        self.SetSize((width, height))

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
