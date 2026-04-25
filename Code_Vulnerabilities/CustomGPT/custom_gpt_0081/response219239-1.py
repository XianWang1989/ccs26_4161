
import wx
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from wx import glcanvas
from OpenGL.GL import *

class MatplotlibPanel(wx.Panel):
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
        self.init = False
        self.context = glcanvas.GLContext(self)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnSize(self, event):
        self.SetCurrent(self.context)
        size = self.GetClientSize()
        glViewport(0, 0, size.width, size.height)
        self.Refresh()

    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()

    def InitGL(self):
        glClearColor(0.2, 0.2, 0.2, 1)
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)

        # Draw a simple cube
        glBegin(GL_QUADS)
        for (color, vertices) in [
            ((1, 0, 0), [(1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1)]),  # Front face
            ((0, 1, 0), [(1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1)]),  # Back face
        ]:
            glColor3f(*color)
            for vertex in vertices:
                glVertex3f(*vertex)
        glEnd()

        self.SwapBuffers()

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Matplotlib and OpenGL in wxPython', size=(800, 400))
        self.panel = wx.Panel(self)

        # Create a horizontal box sizer
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create instances of the Matplotlib panel and OpenGL canvas
        self.matplotlib_panel = MatplotlibPanel(self.panel)
        self.opengl_canvas = OpenGLCanvas(self.panel)

        # Add the panels to the sizer
        sizer.Add(self.matplotlib_panel, 1, wx.EXPAND)
        sizer.Add(self.opengl_canvas, 1, wx.EXPAND)

        self.panel.SetSizer(sizer)
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
