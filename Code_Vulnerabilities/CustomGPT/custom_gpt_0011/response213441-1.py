
import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Set the initial size of the frame
        self.SetInitialSize(self.calculate_size())

        self.Show()

    def calculate_size(self):
        # Get the screen size
        screen_width, screen_height = wx.MetaGetScreenSize()

        # Specify the desired width and height as percentages
        width_percentage = 0.2  # 20%
        height_percentage = 0.2  # 20%

        # Calculate the size in pixels based on the percentage
        width = int(screen_width * width_percentage)
        height = int(screen_height * height_percentage)

        return (width, height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
