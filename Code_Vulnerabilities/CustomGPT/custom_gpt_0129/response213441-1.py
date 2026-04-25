
import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Call to set the size based on percentage of the parent window
        self.SetSizeToPercentage(20, 20)  # 20% of width and height

        self.Show()

    def SetSizeToPercentage(self, width_pct, height_pct):
        # Get the size of the frame (parent)
        width, height = self.GetSize()

        # Calculate new size in pixels based on percentage
        new_width = int(width * (width_pct / 100))
        new_height = int(height * (height_pct / 100))

        # Set the new size
        self.SetSize(new_width, new_height)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size as Percentage')
    app.MainLoop()
