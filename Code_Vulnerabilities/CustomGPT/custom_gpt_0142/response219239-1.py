
import wx
import numpy as np
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *

# Matplotlib canvas class
class MatplotlibCanvas(wx.Panel):
    def __init__(self, parent):
        super(MatplotlibCanvas, self).__init__(parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()

    def draw(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()

# OpenGL canvas class
class OpenGLCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        super(OpenGLCanvas, self).__init__(parent)
        self.context = glcanvas.GLContext(self)
        self.init = False
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def InitGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Set up your OpenGL view here
        glTranslatef(0.0, 0.0, -5)
        glutWireCube(1)  # Draws a wireframe cube
        self.SwapBuffers()

# Main application class
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, wx.ID_ANY, "Matplotlib and OpenGL in wxPython")
        panel = wx.Panel(frame)

        # Create a horizontal sizer to hold both canvases
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create Matplotlib Canvas
        matplotlib_canvas = MatplotlibCanvas(panel)
        matplotlib_canvas.draw()
        sizer.Add(matplotlib_canvas, 1, wx.EXPAND | wx.ALL, 5)

        # Create OpenGL Canvas
        opengl_canvas = OpenGLCanvas(panel)
        sizer.Add(opengl_canvas, 1, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(sizer)
        frame.SetSize((800, 600))
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
