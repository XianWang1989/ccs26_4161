
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
import wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from wx import glcanvas
from OpenGL.GL import *

# Matplotlib Canvas
class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
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
        self.context = glcanvas.GLContext(self)
        self.init = False
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
        glTranslatef(0.0, 0.0, -5)

        # Draw a cube
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)
        for i in [(-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5)]:
            glVertex3f(*i)
        glEnd()
        self.SwapBuffers()

# Main application frame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Matplotlib and OpenGL Integration', size=(800, 600))
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create and add the matplotlib canvas
        self.mat_plot_canvas = CanvasPanel(self)
        self.mat_plot_canvas.draw()
        self.sizer.Add(self.mat_plot_canvas, 1, wx.EXPAND | wx.ALL)

        # Create and add the OpenGL canvas
        self.gl_canvas = MyCanvasBase(self)
        self.sizer.Add(self.gl_canvas, 1, wx.EXPAND | wx.ALL)

        self.SetSizer(self.sizer)
        self.Layout()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
