
import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        # Set initial size of the frame
        self.SetSize(600, 400)

        # Create a Panel
        panel = wx.Panel(self)

        # Get the size of the frame
        width, height = self.GetSize()

        # Calculate size based on percentages
        panel_size_x = int(width * 0.20)  # 20% of width
        panel_size_y = int(height * 0.20) # 20% of height

        # Set the size of the panel
        panel.SetSize(panel_size_x, panel_size_y)

        # Center the panel in the frame
        panel.SetPosition((width // 2 - panel_size_x // 2, height // 2 - panel_size_y // 2))

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
