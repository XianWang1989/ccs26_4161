import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        screen_width, screen_height = wx.GetDisplaySize()
        
        # Define size as percentage
        width_pct = 20
        height_pct = 20

        # Convert percentage to pixels
        width = int(screen_width * width_pct / 100)
        height = int(screen_height * height_pct / 100)

        super(Example, self).__init__(parent, title=title, size=(width, height))
        self.Centre()
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size in %')
    app.MainLoop()
