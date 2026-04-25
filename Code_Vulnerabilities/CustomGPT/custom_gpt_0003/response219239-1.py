
import wx
import matplotlib
matplotlib.use('WXAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *

class MatplotlibPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()
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
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_QUADS)
        glColor3f(1, 0, 0)  # Red
        glVertex3f(-1, -1, 0)
        glVertex3f( 1, -1, 0)
        glVertex3f( 1,  1, 0)
        glVertex3f(-1,  1, 0)
        glEnd()

class MainFrame(wx.Frame):
    def __init__(self):
        super(MainFrame, self).__init__(None, title="wxPython with Matplotlib and OpenGL", size=(800, 600))
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add Matplotlib panel to the left
        self.matplotlib_panel = MatplotlibPanel(self.panel)
        self.sizer.Add(self.matplotlib_panel, 1, wx.EXPAND | wx.ALL, 5)

        # Add OpenGL panel to the right
        self.opengl_canvas = MyCanvasBase(self.panel)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND | wx.ALL, 5)

        self.panel.SetSizer(self.sizer)
        self.SetSizer(self.sizer)
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
