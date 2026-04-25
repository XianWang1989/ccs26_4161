
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import wx
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *

class MatplotlibCanvas(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()
        self.draw()

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()

class OpenGLCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.context = glcanvas.GLContext(self)
        self.init = False

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnSize(self, event):
        self.SetCurrent(self.context)
        size = self.GetClientSize()
        glViewport(0, 0, size.width, size.height)
        event.Skip()

    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.Render()

    def InitGL(self):
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1, 0.1, 50)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def Render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)
        glBegin(GL_QUADS)

        # Draw a cube
        glColor3f(1, 0, 0); glVertex3f(1, 1, -1)
        glColor3f(0, 1, 0); glVertex3f(-1, 1, -1)
        glColor3f(0, 0, 1); glVertex3f(-1, -1, -1)
        glColor3f(1, 1, 0); glVertex3f(1, -1, -1)
        glEnd()

        self.SwapBuffers()

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Matplotlib and OpenGL Example', size=(800, 600))

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create matplotlib and OpenGL canvases
        matplotlib_canvas = MatplotlibCanvas(panel)
        opengl_canvas = OpenGLCanvas(panel)

        sizer.Add(matplotlib_canvas, 1, wx.EXPAND)
        sizer.Add(opengl_canvas, 1, wx.EXPAND)
        panel.SetSizer(sizer)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show(True)
    app.MainLoop()
