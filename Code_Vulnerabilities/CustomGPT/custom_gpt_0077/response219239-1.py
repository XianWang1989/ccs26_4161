
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import wx
from wx import glcanvas
from OpenGL.GL import *

# Matplotlib Canvas
class MatplotlibCanvas(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
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
        self.draw_cube()
        self.SwapBuffers()

    def draw_cube(self):
        glBegin(GL_QUADS)
        # Front face
        glColor3f(1, 0, 0)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        # ... other faces
        glEnd()

# Main Frame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Matplotlib and OpenGL', size=(800, 600))
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.matplotlib_canvas = MatplotlibCanvas(self)
        self.opengl_canvas = MyCanvasBase(self)

        self.sizer.Add(self.matplotlib_canvas, 1, wx.EXPAND)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
