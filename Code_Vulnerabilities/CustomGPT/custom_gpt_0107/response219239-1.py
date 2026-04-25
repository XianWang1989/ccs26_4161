
import wx
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from wx import glcanvas
from OpenGL.GL import *

class MatplotlibCanvas(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.draw()

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()

class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent)
        self.context = glcanvas.GLContext(self)
        self.init = False
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()
        self.SwapBuffers()

    def InitGL(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-0.5, 0.5, 0)
        glVertex3f(0.5, 0.5, 0)
        glVertex3f(0.5, -0.5, 0)
        glVertex3f(-0.5, -0.5, 0)
        glEnd()

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="wxPython with Matplotlib and OpenGL", size=(800, 400))
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create Matplotlib and OpenGL canvases
        self.matplotlib_canvas = MatplotlibCanvas(self)
        self.opengl_canvas = MyCanvasBase(self)

        # Add canvases to sizer
        self.sizer.Add(self.matplotlib_canvas, 1, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(self.sizer)
        self.Layout()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
