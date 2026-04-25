
from numpy import arange, sin, pi
import wx
from wx import glcanvas
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from OpenGL.GL import *
from OpenGL.GLUT import *

# Matplotlib canvas
class MplCanvas(wx.Panel):
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
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.clear()
        self.axes.plot(t, s)
        self.canvas.draw()

# OpenGL canvas
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

    def InitGL(self):
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.DrawCube()
        self.SwapBuffers()

    def DrawCube(self):
        glBegin(GL_QUADS)
        # Define cube vertices and colors
        vertices = [
            [0.5, 0.5, 0.5],  [-0.5, 0.5, 0.5],
            [-0.5, -0.5, 0.5], [0.5, -0.5, 0.5],
            [-0.5, -0.5, -0.5], [-0.5, 0.5, -0.5],
            [0.5, 0.5, -0.5], [0.5, -0.5, -0.5],
        ]
        normals = [
            [0, 0, 1], [0, 0, -1], [0, 1, 0],
            [0, -1, 0], [1, 0, 0], [-1, 0, 0]
        ]
        faces = [
            [0, 1, 2, 3], [4, 5, 6, 7],
            [0, 3, 7, 6], [1, 2, 4, 5],
            [0, 1, 5, 4], [2, 3, 7, 6]
        ]
        for i in range(6):
            glNormal3fv(normals[i])
            for j in faces[i]:
                glVertex3fv(vertices[j])
        glEnd()

# Main application frame combining both canvases
class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Matplotlib and OpenGL Example', size=(800, 600))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.mpl_canvas = MplCanvas(panel)
        self.opengl_canvas = MyCanvasBase(panel)

        sizer.Add(self.mpl_canvas, 1, wx.EXPAND)
        sizer.Add(self.opengl_canvas, 1, wx.EXPAND)

        panel.SetSizer(sizer)
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
