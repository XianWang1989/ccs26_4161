
import wx
import sys
from numpy import arange, sin, pi
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
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()

    def InitGL(self):
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)
        glutWireCube(1)  # Draw a wireframe cube
        self.SwapBuffers()

# Main Frame
class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Matplotlib and OpenGL', size=(800, 600))

        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create and add Matplotlib canvas
        self.matplotlib_canvas = MatplotlibCanvas(self)
        self.matplotlib_canvas.draw()
        sizer.Add(self.matplotlib_canvas, 1, wx.EXPAND)

        # Create and add OpenGL canvas
        self.opengl_canvas = MyCanvasBase(self)
        sizer.Add(self.opengl_canvas, 1, wx.EXPAND)

        self.SetSizer(sizer)
        self.Layout()
        self.Show()

# Run Application
if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
