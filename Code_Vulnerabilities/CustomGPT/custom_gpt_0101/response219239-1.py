
import wx
import matplotlib
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from wx import glcanvas
from OpenGL.GL import *

# Matplotlib Canvas
class MatplotlibCanvas(wx.Panel):
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
        self.axes.plot(t, s)
        self.canvas.draw()

# OpenGL Canvas
class OpenGLCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent)
        self.context = glcanvas.GLContext(self)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.init = False

    def OnSize(self, event):
        size = self.GetClientSize()
        glViewport(0, 0, size.width, size.height)
        self.Refresh()

    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()

    def InitGL(self):
        glClearColor(0, 0, 0, 1)
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        glBegin(GL_QUADS)
        glColor3f(1, 0, 0); glVertex3f(-1, -1, 0)
        glColor3f(0, 1, 0); glVertex3f(1, -1, 0)
        glColor3f(0, 0, 1); glVertex3f(1, 1, 0)
        glColor3f(1, 1, 0); glVertex3f(-1, 1, 0)
        glEnd()
        self.SwapBuffers()

# Main Frame
class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Matplotlib and OpenGL in wxPython', size=(800, 400))
        self.splitter = wx.SplitterWindow(self)
        self.matplotlib_panel = MatplotlibCanvas(self.splitter)
        self.opengl_panel = OpenGLCanvas(self.splitter)
        self.splitter.SplitVertically(self.matplotlib_panel, self.opengl_panel, 300)
        self.splitter.SetSashGravity(0)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
