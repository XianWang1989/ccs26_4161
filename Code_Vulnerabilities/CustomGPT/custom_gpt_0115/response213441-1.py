
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Set the frame size (width, height)
        self.SetSize(800, 600)

        # Calculate the size based on percentages
        width_percent = 0.2  # 20%
        height_percent = 0.2  # 20%

        frame_size = self.GetSize()
        new_size = (
            int(frame_size[0] * width_percent),
            int(frame_size[1] * height_percent)
        )

        # Set the size of the panel or any other component
        panel = wx.Panel(self)
        panel.SetSize(new_size)

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size Percentage Example')
    app.MainLoop()
