
import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Create a panel to hold the resized controls
        panel = wx.Panel(self)

        # Get the current size of the window
        width, height = self.GetSize()

        # Calculate the size in pixels based on a percentage
        percent_width = int(width * 0.2)  # 20% of the width
        percent_height = int(height * 0.2)  # 20% of the height

        # Create a button with the calculated size
        button = wx.Button(panel, label="Click Me", size=(percent_width, percent_height))
        button.SetPosition((width // 2 - percent_width // 2, height // 2 - percent_height // 2))

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
