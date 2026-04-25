
import wx
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import numpy as np

class MatplotlibPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)

        self.draw()

    def draw(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()

class OpenGLCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        super().__init__(parent)
        self.context = glcanvas.GLContext(self)
        self.init = False

        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def InitGL(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def OnPaint(self, event):
        if not self.init:
            self.InitGL()
            self.init = True
        self.SetCurrent(self.context)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.draw_cube()
        self.SwapBuffers()

    def draw_cube(self):
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)  # Red
        for face in [((-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5)),
                      ((0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]:
            for vertex in face:
                glVertex3f(*vertex)
        glEnd()

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='wxPython with Matplotlib and OpenGL', size=(800, 600))

        sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.matplotlib_panel = MatplotlibPanel(self)
        self.opengl_canvas = OpenGLCanvas(self)

        sizer.Add(self.matplotlib_panel, 1, wx.EXPAND)
        sizer.Add(self.opengl_canvas, 1, wx.EXPAND)

        self.SetSizer(sizer)
        self.Layout()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
