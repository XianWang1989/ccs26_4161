
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Get the screen size
        screen_width, screen_height = wx.GetDisplaySize()

        # Define the size in percentage
        width_percent = 0.2  # 20%
        height_percent = 0.2  # 20%

        # Calculate pixel size based on the percentage
        size = (int(screen_width * width_percent), int(screen_height * height_percent))
        self.SetSize(size)

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
