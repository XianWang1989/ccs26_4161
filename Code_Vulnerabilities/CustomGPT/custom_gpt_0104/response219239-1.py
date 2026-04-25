
import wx
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *


class MplCanvas(wx.Panel):
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
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.clear()
        self.axes.plot(t, s)
        self.canvas.draw()


class OpenGLCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = glcanvas.GLContext(self)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.SetCurrent(self.context)

    def OnSize(self, event):
        self.SetCurrent(self.context)
        size = self.GetSize()
        glViewport(0, 0, size.width, size.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (size.width / size.height), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)

    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()

    def InitGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)
        self.DrawCube()
        self.SwapBuffers()

    def DrawCube(self):
        glBegin(GL_QUADS)
        # Define the vertices for a cube
        vertices = [
            [1, 1, -1],
            [1, -1, -1],
            [-1, -1, -1],
            [-1, 1, -1],
            [1, 1, 1],
            [1, -1, 1],
            [-1, -1, 1],
            [-1, 1, 1]
        ]
        for i in range(6):
            for j in range(4):
                glVertex3fv(vertices[j + i * 4 % 4])

        glEnd()


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Combined Mpl and OpenGL Canvas', size=(800, 600))

        splitter = wx.SplitterWindow(self)
        mpl_canvas = MplCanvas(splitter)
        ogl_canvas = OpenGLCanvas(splitter)

        splitter.SplitVertically(mpl_canvas, ogl_canvas, 400)
        splitter.SetSashPosition(400)
        splitter.SetMinimumPaneSize(100)
        splitter.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.Show()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
