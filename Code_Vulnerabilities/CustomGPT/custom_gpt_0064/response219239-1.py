
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import wx
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *


class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create matplotlib canvas
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)

        # Create OpenGL canvas
        self.opengl_canvas = CubeCanvas(self)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND)

        self.SetSizer(self.sizer)
        self.Fit()

        self.draw_matplotlib()

    def draw_matplotlib(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()


class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = glcanvas.GLContext(self)

        # Initial mouse position
        self.lastx = self.x = 30
        self.lasty = self.y = 30
        self.size = None
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()
        self.SwapBuffers()

    def InitGL(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1.0, 1.0, -1.0, 1.0, 1.0, 10.0)
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(0.0, 0.0, -5.0)
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_QUADS)
        # Draw a cube (same as your existing cube drawing)
        glNormal3f(0.0, 0.0, 1.0)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f(0.5, -0.5, 0.5)
        glEnd()

        # Implement any rotation or other transformations here

class CubeCanvas(MyCanvasBase):
    def OnPaint(self, event):
        super().OnPaint(event)


class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='Matplotlib and OpenGL in wxPython')
        panel = CanvasPanel(frame)
        frame.Show()
        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
