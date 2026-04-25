
import wx
import sys
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *

# Matplotlib Panel
class MatplotlibPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
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
        self.axes.plot(t, s)
        self.canvas.draw()

# OpenGL Canvas
class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        super().__init__(parent, -1)
        self.context = glcanvas.GLContext(self)
        self.init = False
        self.lastx, self.lasty = 30, 30
        self.size = None
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()

    def InitGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1, 0.1, 50)
        glMatrixMode(GL_MODELVIEW)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        glRotatef(self.lastx, 1, 0, 0)
        glRotatef(self.lasty, 0, 1, 0)

        # Draw Cube
        glBegin(GL_QUADS)
        for face in [[(0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5)],
                     [(0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5)],
                     [(-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5)],
                     [(0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, -0.5, -0.5)],
                     [(0.5, 0.5, -0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, 0.5, -0.5)],
                     [(0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5)]]:
            for vertex in face:
                glVertex3f(*vertex)
        glEnd()

        self.SwapBuffers()

# Main Frame
class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Matplotlib and OpenGL', size=(800, 400))
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.matplotlib_panel = MatplotlibPanel(self)
        self.opengl_canvas = MyCanvasBase(self)
        self.sizer.Add(self.matplotlib_panel, 1, wx.EXPAND)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
