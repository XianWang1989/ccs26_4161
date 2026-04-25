
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(600, 400))

        # Get the size of the frame
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Centre()
        self.Show()

    def on_size(self, event):
        # Get current size of the frame
        width, height = self.GetSize()

        # Calculate sizes as percentages of the frame size
        button_width = int(width * 0.2)  # 20%
        button_height = int(height * 0.2)  # 20%

        # Create a button with the calculated size
        button = wx.Button(self, label='Click Me', size=(button_width, button_height))

        # Center the button
        button.Centre()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size Example')
    app.MainLoop()
