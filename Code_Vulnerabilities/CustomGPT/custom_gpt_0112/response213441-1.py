
import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(800, 600))

        # Set the size using percentages
        self.SetSize(self.calculate_size(20, 20))
        self.Show()

    def calculate_size(self, width_percent, height_percent):
        # Get the size of the screen
        screen_size = wx.GetClientSize()
        width = int(screen_size.GetWidth() * (width_percent / 100))
        height = int(screen_size.GetHeight() * (height_percent / 100))
        return (width, height)

if __name__ == '__main__':
    app = wx.App(False)
    Example(None, title='Size in Percentage')
    app.MainLoop()
