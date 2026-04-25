
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
        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        # Initialize the plot
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
        self.OnDraw()

    def InitGL(self):
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1, 1, 100)
        glMatrixMode(GL_MODELVIEW)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)
        self.DrawCube()
        self.SwapBuffers()

    def DrawCube(self):
        glBegin(GL_QUADS)
        # Define vertices and normal for each face of the cube
        for i, color in enumerate([(1,0,0), (0,1,0), (0,0,1), (1,1,0), (1,0,1), (0,1,1)]):
            glColor3fv(color)
            if i == 0:
                vertices = [(1, 1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1)]  # Front
            elif i == 1:
                vertices = [(-1, -1, -1), (-1, 1, -1), (1, 1, -1), (1, -1, -1)]  # Back
            elif i == 2:
                vertices = [(1, 1, 1), (1, 1, -1), (-1, 1, -1), (-1, 1, 1)]  # Top
            elif i == 3:
                vertices = [(-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1)]  # Bottom
            elif i == 4:
                vertices = [(1, 1, 1), (1, -1, 1), (1, -1, -1), (1, 1, -1)]  # Right
            else:
                vertices = [(-1, -1, -1), (-1, -1, 1), (-1, 1, 1), (-1, 1, -1)]  # Left

            for vertex in vertices:
                glVertex3fv(vertex)
        glEnd()


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Matplotlib and OpenGL in WXPython", size=(800, 400))
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create instances of the canvases
        self.matplotlib_canvas = CanvasPanel(self.panel)
        self.opengl_canvas = MyCanvasBase(self.panel)

        self.sizer.Add(self.matplotlib_canvas, 1, wx.EXPAND | wx.ALL)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND | wx.ALL)
        self.panel.SetSizer(self.sizer)

        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
