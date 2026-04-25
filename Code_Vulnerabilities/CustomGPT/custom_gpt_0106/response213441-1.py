
import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Bind the OnSize method to get the size changes
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.panel = wx.Panel(self)

        # Initially set the size of the panel as per percentage
        self.SetPanelSize(0.2, 0.2)  # 20% width and height

        self.Show()

    def OnSize(self, event):
        # Adjust the size of the panel when the frame is resized
        self.SetPanelSize(0.2, 0.2)  # 20% width and height
        event.Skip()

    def SetPanelSize(self, width_percent, height_percent):
        frame_size = self.GetSize()
        new_width = int(frame_size[0] * width_percent)
        new_height = int(frame_size[1] * height_percent)
        self.panel.SetSize(new_width, new_height)
        self.panel.SetBackgroundColour(wx.Colour(100, 100, 250))  # Set a background color

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
