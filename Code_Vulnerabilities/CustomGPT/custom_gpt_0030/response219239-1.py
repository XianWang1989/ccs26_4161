
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

        # Create a sizer to arrange the canvases
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create matplotlib canvas
        self.matplotlib_canvas = MatplotlibCanvas(self)
        self.sizer.Add(self.matplotlib_canvas, 1, wx.EXPAND | wx.ALL, 5)

        # Create OpenGL canvas
        self.opengl_canvas = CubeCanvas(self)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(self.sizer)
        self.Fit()


class MatplotlibCanvas(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.draw()

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()


class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = glcanvas.GLContext(self)

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

    def InitGL(self):
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1, 1, 100)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.DrawCube()
        self.SwapBuffers()

    def DrawCube(self):
        glBegin(GL_QUADS)
        # Front face
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f( 1,  1, 1)
        glVertex3f(-1,  1, 1)
        glVertex3f(-1, -1, 1)
        glVertex3f( 1, -1, 1)
        # (Add other faces here)
        glEnd()


class CubeCanvas(MyCanvasBase):
    # Additional OpenGL setup or drawing code can go here if necessary
    pass


class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='wxPython with Matplotlib and OpenGL', size=(800, 600))
        panel = CanvasPanel(frame)
        frame.Show()
        return True


if __name__ == "__main__":
    app = App()
    app.MainLoop()
