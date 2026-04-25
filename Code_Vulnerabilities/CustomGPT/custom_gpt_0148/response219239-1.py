
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import wx
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *

# Matplotlib canvas class
class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()

# OpenGL canvas class
class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        super().__init__(parent)
        self.init = False
        self.context = glcanvas.GLContext(self)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.Render()

    def InitGL(self):
        glEnable(GL_DEPTH_TEST)

    def Render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_QUADS)
        glVertex3f(-0.5, -0.5, 0.0)
        glVertex3f(0.5, -0.5, 0.0)
        glVertex3f(0.5, 0.5, 0.0)
        glVertex3f(-0.5, 0.5, 0.0)
        glEnd()
        self.SwapBuffers()

# Main frame class
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Matplotlib and OpenGL', size=(800, 600))
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create matplotlib and OpenGL canvases
        self.matplotlib_canvas = CanvasPanel(self.panel)
        self.opengl_canvas = MyCanvasBase(self.panel)

        # Add canvases to sizer
        self.sizer.Add(self.matplotlib_canvas, 1, wx.EXPAND)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND)

        self.panel.SetSizer(self.sizer)
        self.matplotlib_canvas.draw()

# Run the application
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
