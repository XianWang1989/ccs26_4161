
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(800, 600))

        # Set the size using percentages
        self.SetSize(self.calculate_size(20, 20))

        self.Show()

    def calculate_size(self, width_percent, height_percent):
        screen_size = wx.GetDisplaySize()
        width = int(screen_size.width * (width_percent / 100))
        height = int(screen_size.height * (height_percent / 100))
        return (width, height)

if __name__ == '__main__':
    app = wx.App(False)
    Example(None, title='Size in Percentages')
    app.MainLoop()
