
import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Set the initial size of the frame
        self.SetSize((600, 400))

        # Calculate size based on percentage
        percentage_width = 20  # 20% of the parent size
        percentage_height = 20  # 20% of the parent size

        # Get the size of the parent (here it's the screen size)
        screen_width, screen_height = wx.GetDisplaySize()

        # Calculate new dimensions
        new_width = int(screen_width * (percentage_width / 100))
        new_height = int(screen_height * (percentage_height / 100))

        # Set size to new dimensions
        self.SetSize((new_width, new_height))

        self.Show()


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
