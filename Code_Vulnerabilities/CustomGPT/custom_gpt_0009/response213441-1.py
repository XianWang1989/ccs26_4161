
import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Create a panel in the frame
        panel = wx.Panel(self)

        # Create a box sizer
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Creating a button
        button = wx.Button(panel, label="Button")

        # Add button with percentage size (20% of the panel's width)
        sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)

        # Set the sizer to the panel
        panel.SetSizer(sizer)

        # Adjust the button size to 20% of the panel's width
        panel.Bind(wx.EVT_SIZE, self.on_size)

        self.Show()

    def on_size(self, event):
        panel = self.FindWindowById(wx.ID_ANY)
        button = panel.GetChildren()[0]  # Assuming the button is the first child
        panel_width = panel.GetSize()[0]

        # Set button size to 20% of panel width and the default height
        button.SetSize((int(panel_width * 0.2), button.GetSize()[1]))

        # Refresh the panel to update layout
        panel.Layout()
        event.Skip()


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
