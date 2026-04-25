
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import wx
from wx import glcanvas
from OpenGL.GL import *

class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Create the Matplotlib canvas
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.draw_plot()

        # Create the OpenGL canvas
        self.gl_canvas = CubeCanvas(self)

        # Arrange the canvases using BoxSizer
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.sizer.Add(self.gl_canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()

    def draw_plot(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)

class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent)
        self.context = glcanvas.GLContext(self)
        self.init = False

        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
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
        glTranslatef(0.0, 0.0, -5.0)

        # Draw a rotating cube
        glBegin(GL_QUADS)
        # Front face
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f( 1.0, -1.0, 1.0)
        glVertex3f( 1.0,  1.0, 1.0)
        glVertex3f(-1.0,  1.0, 1.0)
        # Additional faces go here...
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
