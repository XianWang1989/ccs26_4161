
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Get the size of the frame
        self.Bind(wx.EVT_SIZE, self.on_resize)

        self.panel = wx.Panel(self)
        self.SetBackgroundColour('white')

        self.Show()

    def on_resize(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate sizes as percentages
        panel_width = int(width * 0.2)  # 20% of the width
        panel_height = int(height * 0.2)  # 20% of the height

        # Set the size of the panel
        self.panel.SetSize(panel_width, panel_height)
        self.panel.SetPosition((width * 0.4, height * 0.4))  # Centering the panel

        self.Layout()  # Refresh the layout

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size in Percent')
    app.MainLoop()
