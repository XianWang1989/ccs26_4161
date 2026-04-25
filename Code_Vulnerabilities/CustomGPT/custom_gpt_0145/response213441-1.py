
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))

        # Bind the size event so we can adjust on resize
        self.Bind(wx.EVT_SIZE, self.on_resize)
        self.panel = wx.Panel(self)
        self.layout_elements()

        self.Show()

    def layout_elements(self):
        # Get the current size of the frame
        width, height = self.GetSize()

        # Calculate the size as a percentage
        panel_width = int(width * 0.20)    # 20% of the width
        panel_height = int(height * 0.20)  # 20% of the height

        # Set the size of the panel
        self.panel.SetSize(panel_width, panel_height)

    def on_resize(self, event):
        # Recalculate the sizes on resize
        self.layout_elements()
        event.Skip()  # ensure that other resize events are processed

if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Size with Percentage')
    app.MainLoop()
