
import wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from OpenGL.GL import *
from OpenGL.GLUT import *
from wx import glcanvas
import numpy as np

# Create a wxPython panel for the Matplotlib canvas
class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)

        # Draw a simple sine wave
        self.draw_figure()

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def draw_figure(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()

# Create a wxPython panel for the OpenGL canvas
class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        self.context = glcanvas.GLContext(self)
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
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

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)

        # Draw a simple cube
        glutWireCube(1)
        self.SwapBuffers()

# Main application
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='Matplotlib & OpenGL Example', size=(800, 400))

        # Create a horizontal box sizer
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add Matplotlib canvas
        matplot_panel = CanvasPanel(frame)
        sizer.Add(matplot_panel, 1, wx.EXPAND)

        # Add OpenGL canvas
        gl_panel = MyCanvasBase(frame)
        sizer.Add(gl_panel, 1, wx.EXPAND)

        frame.SetSizer(sizer)
        frame.Show()
        return True

app = MyApp()
app.MainLoop()
