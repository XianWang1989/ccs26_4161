
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import wx
import wx.glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *

# Define the Matplotlib Canvas
class MatplotlibCanvas(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)

        self.draw()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()

# Define the OpenGL Canvas
class OpenGLCanvas(wx.glcanvas.GLCanvas):
    def __init__(self, parent):
        wx.glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = wx.glcanvas.GLContext(self)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def InitGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1, 1, -1, 1, 1.5, 10)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.SetCurrent(self.context)

        if not self.init:
            self.InitGL()
            self.init = True

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)

        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, 1.0)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glEnd()

        self.SwapBuffers()

# Main Application Frame
class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Matplotlib & OpenGL', size=(800, 400))
        panel = wx.Panel(self)

        # Create sizer for layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add Matplotlib Canvas
        self.matplotlib_canvas = MatplotlibCanvas(panel)
        sizer.Add(self.matplotlib_canvas, 1, wx.EXPAND | wx.ALL)

        # Add OpenGL Canvas
        self.opengl_canvas = OpenGLCanvas(panel)
        sizer.Add(self.opengl_canvas, 1, wx.EXPAND | wx.ALL)

        panel.SetSizer(sizer)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
