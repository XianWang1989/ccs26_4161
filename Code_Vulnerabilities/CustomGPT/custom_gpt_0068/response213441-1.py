
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(250, 200))

        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.panel = wx.Panel(self)

        # Create a child window (for example, another panel) 
        self.child_panel = wx.Panel(self.panel, size=(0, 0))
        self.child_panel.SetBackgroundColour(wx.Colour(255, 0, 0))  # Red panel for visibility

        self.SetBackgroundColour(wx.Colour(200, 200, 200))  # Background color
        self.Show()

    def on_resize(self, event):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate sizes based on percentage
        new_width = int(width * 0.2)  # 20% of the width
        new_height = int(height * 0.2)  # 20% of the height

        # Resize the child panel
        self.child_panel.SetSize(new_width, new_height)

        # Optional: Center the child panel
        self.child_panel.SetPosition((width * 0.4, height * 0.4))  # Centering child panel

        # Refresh to update the display
        self.Layout()

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size with Percentage')
    app.MainLoop()
