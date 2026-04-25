
import wx
import sys
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *

# Matplotlib Canvas
class MatplotlibCanvas(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()
        self.draw()

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()

# OpenGL Canvas
class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = glcanvas.GLContext(self)

        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()
        self.SwapBuffers()

    def InitGL(self):
        glMatrixMode(GL_PROJECTION)
        glFrustum(-0.5, 0.5, -0.5, 0.5, 1.0, 3.0)
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(0.0, 0.0, -2.0)
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_QUADS)
        # Draw cube
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f(0.5, -0.5, 0.5)
        glEnd()

# Main Frame
class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Matplotlib and OpenGL", size=(800, 400))
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create canvases
        self.matplotlib_canvas = MatplotlibCanvas(self)
        self.opengl_canvas = MyCanvasBase(self)

        self.sizer.Add(self.matplotlib_canvas, 1, wx.EXPAND | wx.ALL)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND | wx.ALL)

        self.SetSizer(self.sizer)
        self.Layout()

# Run the application
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
