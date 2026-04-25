
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import wx
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *


# Matplotlib Canvas Class
class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)

        # Layout
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()


# OpenGL Canvas Class
class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = glcanvas.GLContext(self)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()
        self.SwapBuffers()

    def InitGL(self):
        glClearColor(0.5, 0.5, 0.5, 1.0)  # Set clear color
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)  # Move back
        glutWireCube(1)  # Draw a wireframe cube


# Main Application Frame
class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Matplotlib & OpenGL', size=(800, 400))

        # Create a panel to hold both canvases
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add Matplotlib canvas
        self.matplotlib_panel = CanvasPanel(panel)
        self.matplotlib_panel.draw()
        sizer.Add(self.matplotlib_panel, 1, wx.EXPAND)

        # Add OpenGL canvas
        self.opengl_canvas = MyCanvasBase(panel)
        sizer.Add(self.opengl_canvas, 1, wx.EXPAND)

        panel.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
