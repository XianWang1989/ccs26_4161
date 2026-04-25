
import wx
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from wx import glcanvas
from OpenGL.GL import *

# Matplotlib Canvas Class
class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()

    def draw(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()

# OpenGL Canvas Class
class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent)
        self.init = False
        self.context = glcanvas.GLContext(self)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()

    def InitGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        self.draw_cube()
        self.SwapBuffers()

    def draw_cube(self):
        glBegin(GL_QUADS)
        # Define vertices for a cube
        vertices = [
            (1, 1, -1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1), # Front
            (1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1) # Back
        ]
        faces = [
            (0, 1, 2, 3), (4, 5, 6, 7), # Front and Back
            (0, 3, 7, 4), (1, 2, 6, 5), # Left and Right
            (3, 2, 6, 7), (0, 1, 5, 4)  # Top and Bottom
        ]
        for face in faces:
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()

# Main Frame Class
class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Matplotlib and OpenGL in wxPython', size=(800, 400))
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create instances of both canvases
        self.matplotlib_panel = CanvasPanel(self.panel)
        self.opengl_canvas = MyCanvasBase(self.panel)

        # Add both canvases to the sizer
        self.sizer.Add(self.matplotlib_panel, 1, wx.EXPAND)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND)
        self.panel.SetSizer(self.sizer)

        # Draw the matplotlib graph
        self.matplotlib_panel.draw()

# Run the Application
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
