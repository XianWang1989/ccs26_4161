
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(800, 600))

        # Set the size based on percentages
        self.set_size_percentage(20, 20)

        self.Show()

    def set_size_percentage(self, width_percent, height_percent):
        # Get current size of the frame
        frame_width, frame_height = self.GetSize()

        # Calculate new size based on percentages
        new_width = int(frame_width * (width_percent / 100))
        new_height = int(frame_height * (height_percent / 100))

        # Set the new size
        self.SetSize(new_width, new_height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
