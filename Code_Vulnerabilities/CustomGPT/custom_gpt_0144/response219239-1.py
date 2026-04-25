import wx
from wx import glcanvas
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import arange, sin, pi
from OpenGL.GL import *

# Matplotlib canvas panel
class MatplotlibCanvas(wx.Panel):
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

# OpenGL canvas panel
class OpenGLCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        super().__init__(parent)
        self.context = glcanvas.GLContext(self)
        self.init = False
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnSize(self, event):
        self.SetCurrent(self.context)
        size = self.GetClientSize()
        glViewport(0, 0, size.width, size.height)
        event.Skip()

    def InitGL(self):
        glClearColor(0, 0, 0, 1)
        glEnable(GL_DEPTH_TEST)

    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()
        self.SwapBuffers()

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_TRIANGLES)
        glColor3f(1, 0, 0)
        glVertex3f(-0.6, -0.4, 0)
        glColor3f(0, 1, 0)
        glVertex3f(0.6, -0.4, 0)
        glColor3f(0, 0, 1)
        glVertex3f(0, 0.6, 0)
        glEnd()

# Main application frame
class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Matplotlib and OpenGL in wxPython", size=(800, 400))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.matplotlib_panel = MatplotlibCanvas(panel)
        self.opengl_canvas = OpenGLCanvas(panel)

        sizer.Add(self.matplotlib_panel, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.opengl_canvas, 1, wx.EXPAND | wx.ALL, 5)
        panel.SetSizer(sizer)

# Run the app
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
