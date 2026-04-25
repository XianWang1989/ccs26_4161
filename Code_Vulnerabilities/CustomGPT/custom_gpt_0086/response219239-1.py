
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
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

        # Layout for the Matplotlib canvas
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND | wx.ALL, 5)
        self.opengl_canvas = CubeCanvas(self)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(self.sizer)
        self.Fit()
        self.draw()

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()


class CubeCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.context = glcanvas.GLContext(self)
        self.init = False
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.Draw()

    def InitGL(self):
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1, 0.1, 50)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -5)

    def Draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_QUADS)

        # Define cube vertices
        vertices = [
            [1, 1, -1], [1, -1, -1], [-1, -1, -1], [-1, 1, -1], # Back face
            [1, 1, 1], [1, -1, 1], [-1, -1, 1], [-1, 1, 1] # Front face
        ]
        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0), # Back face
            (4, 5), (5, 6), (6, 7), (7, 4), # Front face
            (0, 4), (1, 5), (2, 6), (3, 7)  # Connect front and back
        ]

        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])

        glEnd()
        self.SwapBuffers()


class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='Matplotlib and OpenGL in wxPython')
        panel = CanvasPanel(frame)
        frame.Show()
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
