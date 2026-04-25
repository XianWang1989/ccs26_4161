
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import wx
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *

# Matplotlib Canvas Class
class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()


# OpenGL Canvas Class
class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = glcanvas.GLContext(self)
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

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)
        glBegin(GL_QUADS)
        glColor3f(1, 0, 0)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)
        glEnd()
        self.SwapBuffers()


# Main Application Class
class MyApp(wx.App):
    def OnInit(self):
        self.frame = wx.Frame(None, title='wxPython, Matplotlib, and OpenGL', size=(800, 400))
        self.panel = wx.Panel(self.frame)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Matplotlib canvas
        self.matplotlib_canvas = CanvasPanel(self.panel)
        self.matplotlib_canvas.draw()  # Draw the graph

        # OpenGL canvas
        self.opengl_canvas = MyCanvasBase(self.panel)

        # Add canvases to sizer
        self.sizer.Add(self.matplotlib_canvas, 1, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND | wx.ALL, 5)

        # Set sizer and show frame
        self.panel.SetSizer(self.sizer)
        self.frame.Show()
        return True


# Run the application
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
