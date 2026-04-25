
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
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)

        # Matplotlib canvas
        self.canvas = FigureCanvas(self, -1, self.figure)

        # OpenGL canvas
        self.opengl_canvas = CubeCanvas(self)

        # Sizer to arrange both canvases
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.canvas, 1, wx.EXPAND | wx.ALL)
        sizer.Add(self.opengl_canvas, 1, wx.EXPAND | wx.ALL)

        self.SetSizer(sizer)
        self.Fit()

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
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()

    def InitGL(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 0.0)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # Example OpenGL drawing (a cube - specific implementation not shown)
        self.SwapBuffers()


class CubeCanvas(MyCanvasBase):
    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw a simple cube
        glBegin(GL_QUADS)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f( 0.5, -0.5, -0.5)
        glVertex3f( 0.5,  0.5, -0.5)
        glVertex3f(-0.5,  0.5, -0.5)
        glEnd()

        self.SwapBuffers()


class RunDemoApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, -1, 'Matplotlib and OpenGL', size=(800, 600))
        panel = CanvasPanel(frame)
        panel.draw()  # Call draw method to plot initially
        frame.Show(True)
        return True


if __name__ == "__main__":
    app = RunDemoApp()
    app.MainLoop()
