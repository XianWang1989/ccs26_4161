
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import wx
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *

# Create a Panel Class for Matplotlib
class MatplotlibPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.clear()  # Clear axes to avoid overlapping plots
        self.axes.plot(t, s)
        self.canvas.draw()

# Create a Base Class for OpenGL Canvas
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
        glEnable(GL_DEPTH_TEST)

# Create a Cube Class for OpenGL
class CubeCanvas(MyCanvasBase):
    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(0.0, 0.0, -5.0)
        # Draw the cube
        glBegin(GL_QUADS)
        for face in [[(1, 1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1)],
                     [(1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1)]]:
            for vertex in face:
                glVertex3fv(vertex)
        glEnd()

# Create the Main Frame
class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Matplotlib and OpenGL in wxPython', size=(800, 400))

        self.panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.matplotlib_panel = MatplotlibPanel(self.panel)
        self.opengl_canvas = CubeCanvas(self.panel)

        sizer.Add(self.matplotlib_panel, 1, wx.EXPAND)
        sizer.Add(self.opengl_canvas, 1, wx.EXPAND)

        self.panel.SetSizer(sizer)
        self.matplotlib_panel.draw()  # Draw initial plot

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
