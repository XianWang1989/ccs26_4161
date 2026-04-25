
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

        # Create sizer to hold matplotlib and OpenGL canvases
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(self.sizer)

        # Create matplotlib canvas
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.matplotlib_canvas = FigureCanvas(self, -1, self.figure)
        self.sizer.Add(self.matplotlib_canvas, 1, wx.EXPAND)

        # Create OpenGL canvas
        self.opengl_canvas = CubeCanvas(self)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND)

        self.Fit()
        self.draw()

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.figure.canvas.draw()

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

class CubeCanvas(MyCanvasBase):
    def InitGL(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1.0, 1.0, -1.0, 1.0, 1.0, 10.0)
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(0.0, 0.0, -5.0)
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_QUADS)  # Draw a cube
        glColor3f(1, 0, 0); glVertex3f( 1, 1, 1)
        glColor3f(0, 1, 0); glVertex3f(-1, 1, 1)
        glColor3f(0, 0, 1); glVertex3f(-1,-1, 1)
        glColor3f(1, 1, 0); glVertex3f( 1,-1, 1)
        glEnd()
        self.SwapBuffers()

class RunDemoApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, -1, 'wxPython with Matplotlib and OpenGL', size=(800, 600))
        panel = CanvasPanel(frame)
        frame.Show(True)
        return True

app = RunDemoApp()
app.MainLoop()
