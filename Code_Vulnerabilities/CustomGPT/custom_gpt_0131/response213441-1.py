
import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(600, 400))

        # Get the size of the frame after it's been shown
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Show()

    def on_size(self, event):
        # Get current size of the frame
        width, height = self.GetSize()

        # Calculate desired sizes based on percentages
        width_percent = int(width * 0.2)  # 20% of frame width
        height_percent = int(height * 0.2)  # 20% of frame height

        # Set the size of a panel or other widget with calculated sizes
        panel = wx.Panel(self)
        panel.SetSize((width_percent, height_percent))
        panel.SetBackgroundColour(wx.Colour(100, 100, 250))  # Example color

        self.Layout()  # Refresh layout

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
