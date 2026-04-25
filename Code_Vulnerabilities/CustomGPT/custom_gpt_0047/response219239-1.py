
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

import wx
from wx import glcanvas
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from OpenGL.GL import *
from OpenGL.GLUT import *

class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Create a sizer for layout
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create and add Matplotlib canvas
        self.matplotlib_canvas = MatplotlibCanvas(self)
        self.sizer.Add(self.matplotlib_canvas, 1, wx.EXPAND)

        # Create and add OpenGL canvas
        self.opengl_canvas = CubeCanvas(self)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND)

        self.SetSizer(self.sizer)

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
        self.SwapBuffers()

class CubeCanvas(MyCanvasBase):
    def InitGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        glLoadIdentity()

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1, 1, -1, 1, 1, 10)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -5)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_QUADS)

        # Define vertices for a cube
        for color, vertices in [
            ((1, 0, 0), [(1, 1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1)]),
            ((0, 1, 0), [(1, -1, -1), (-1, -1, -1), (-1, 1, -1), (1, 1, -1)]),
            ((0, 0, 1), [(1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1)]),
            ((1, 1, 0), [(-1, -1, -1), (-1, -1, 1), (-1, 1, 1), (-1, 1, -1)]),
            ((1, 0, 1), [(1, 1, 1), (1, 1, -1), (-1, 1, -1), (-1, 1, 1)]),
            ((0, 1, 1), [(-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1)])
        ]:
            glColor3f(*color)
            for vertex in vertices:
                glVertex3f(*vertex)

        glEnd()

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='Matplotlib and OpenGL Example', size=(800, 400))
        self.canvas_panel = CanvasPanel(frame)
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
