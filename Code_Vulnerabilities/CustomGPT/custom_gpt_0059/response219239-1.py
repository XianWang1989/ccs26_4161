
import wx
import numpy as np
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
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
        self.draw()

    def draw(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
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
        size = self.GetClientSize()
        self.SetCurrent(self.context)
        glViewport(0, 0, size.width, size.height)

    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.initGL()
            self.init = True
        self.render()

    def initGL(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, 1, 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_QUADS)
        for face in [((1, 1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1)),  # Front
                     ((-1, -1, -1), (-1, 1, -1), (1, 1, -1), (1, -1, -1)),  # Back
                     ((1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1)),  # Right
                     ((-1, -1, -1), (-1, -1, 1), (-1, 1, 1), (-1, 1, -1)),  # Left
                     ((1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1)),  # Top
                     ((-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1))]:  # Bottom
            for vertex in face:
                glVertex3fv(vertex)
        glEnd()
        self.SwapBuffers()

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Matplotlib and OpenGL in wxPython", size=(800, 400))
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.matplotlib_canvas = MatplotlibCanvas(self.panel)
        self.opengl_canvas = OpenGLCanvas(self.panel)

        self.sizer.Add(self.matplotlib_canvas, 1, wx.EXPAND)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND)
        self.panel.SetSizer(self.sizer)
        self.Show()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
