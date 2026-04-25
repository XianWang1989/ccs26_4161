
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
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(self.sizer)
        self.Fit()

        self.draw()

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.clear()  # Clear the axes to redraw the plot
        self.axes.plot(t, s)
        self.canvas.draw()

class MyGLCanvas(glcanvas.GLCanvas):
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
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (self.GetWidth() / self.GetHeight()), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        glBegin(GL_QUADS)

        # Draw a cube or any OpenGL shape you want (here a simple cube)
        # Define vertices for the sides of the cube
        glColor3f(1, 0, 0)  # Red
        for x in [-1, 1]:
            for y in [-1, 1]:
                glVertex3f(x, y, -1)

        glEnd()
        self.SwapBuffers()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Matplotlib and OpenGL in wxPython', size=(800, 600))

        # Create a sizer to arrange the canvases
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create matplotlib canvas and OpenGL canvas
        self.matplotlib_canvas = MatplotlibCanvas(self)
        self.opengl_canvas = MyGLCanvas(self)

        # Add both canvases to the sizer
        sizer.Add(self.matplotlib_canvas, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.opengl_canvas, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(sizer)
        self.Layout()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
