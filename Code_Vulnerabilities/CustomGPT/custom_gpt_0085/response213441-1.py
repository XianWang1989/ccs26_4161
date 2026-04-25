
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(800, 600))

        # Calculate sizes based on percentages
        width_percentage = 0.2  # 20%
        height_percentage = 0.2  # 20%

        # Get the size of the frame
        frame_size = self.GetSize()
        new_size = (
            int(frame_size[0] * width_percentage),
            int(frame_size[1] * height_percentage)
        )

        # Create a panel with calculated size
        panel = wx.Panel(self, size=new_size)
        panel.SetBackgroundColour('light blue')

        self.Centre()
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size in Percentages')
    app.MainLoop()
