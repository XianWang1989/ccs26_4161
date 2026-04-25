
import wx
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import arange, sin, pi

from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *

class MatplotlibCanvas(wx.Panel):
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


class OpenGLCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent)
        self.init = False
        self.context = glcanvas.GLContext(self)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnSize(self, event):
        size = self.GetSize()
        glViewport(0, 0, size.width, size.height)
        self.Refresh()

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.DrawCube()

    def InitGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

    def DrawCube(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)
        glRotatef(30, 1, 1, 0)

        glBegin(GL_QUADS)
        glColor3f(1, 0, 0)  # Red
        glVertex3f(-1, -1, -1)
        glVertex3f( 1, -1, -1)
        glVertex3f( 1,  1, -1)
        glVertex3f(-1,  1, -1)

        glColor3f(0, 1, 0)  # Green
        glVertex3f(-1, -1,  1)
        glVertex3f( 1, -1,  1)
        glVertex3f( 1,  1,  1)
        glVertex3f(-1,  1,  1)

        # Colors and vertices for the other faces would go here...
        glEnd()

        self.SwapBuffers()


class CombinedFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Matplotlib & OpenGL Example', size=(800, 600))
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.matplotlib_canvas = MatplotlibCanvas(self.panel)
        self.matplotlib_canvas.draw()

        self.opengl_canvas = OpenGLCanvas(self.panel)

        self.sizer.Add(self.matplotlib_canvas, 1, wx.EXPAND | wx.ALL)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND | wx.ALL)

        self.panel.SetSizer(self.sizer)

if __name__ == "__main__":
    app = wx.App(False)
    frame = CombinedFrame()
    frame.Show()
    app.MainLoop()
