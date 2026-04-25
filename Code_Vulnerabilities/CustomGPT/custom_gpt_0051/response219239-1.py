
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

        # Create a sizer to organize the two canvases
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Matplotlib Canvas
        self.mpl_canvas = MatplotlibCanvas(self)
        sizer.Add(self.mpl_canvas, 1, wx.EXPAND)

        # OpenGL Canvas
        self.gl_canvas = CubeCanvas(self)
        sizer.Add(self.gl_canvas, 1, wx.EXPAND)

        self.SetSizer(sizer)
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

        # Bind events
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
        glViewport(0, 0, self.GetSize()[0], self.GetSize()[1])
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (self.GetSize()[0] / self.GetSize()[1]), 1, 100)
        glMatrixMode(GL_MODELVIEW)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)

        glBegin(GL_QUADS)
        for (r, g, b) in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0)]:
            glColor3f(r, g, b)
            glVertex3f(1, 1, 0)
            glVertex3f(-1, 1, 0)
            glVertex3f(-1, -1, 0)
            glVertex3f(1, -1, 0)
        glEnd()

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='Matplotlib and OpenGL', size=(800, 600))
        panel = CanvasPanel(frame)
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
