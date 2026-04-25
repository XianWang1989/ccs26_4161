
import wx
import sys
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)

        # Setting up the layout
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)

        # OpenGL Canvas
        self.glcanvas = CubeCanvas(self)
        self.sizer.Add(self.glcanvas, 1, wx.EXPAND)

        self.SetSizer(self.sizer)
        self.Fit()

        self.draw_plot()  # Draw the initial plot

    def draw_plot(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()


class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = glcanvas.GLContext(self)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnEraseBackground(self, event):
        pass

    def OnSize(self, event):
        wx.CallAfter(self.DoSetViewport)
        event.Skip()

    def DoSetViewport(self):
        size = self.GetClientSize()
        self.SetCurrent(self.context)
        glViewport(0, 0, size.width, size.height)

    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()

class CubeCanvas(MyCanvasBase):
    def InitGL(self):
        glMatrixMode(GL_PROJECTION)
        glFrustum(-1.0, 1.0, -1.0, 1.0, 1.0, 10.0)
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(0.0, 0.0, -5.0)
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_QUADS)
        # Define the cube vertices
        glNormal3f(0.0, 0.0, 1.0)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        # Repeat for other faces...
        glEnd()
        self.SwapBuffers()


class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='Matplotlib and OpenGL', size=(800, 600))
        panel = CanvasPanel(frame)
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
