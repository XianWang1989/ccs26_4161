
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from wx import glcanvas
from OpenGL.GL import *
import wx

# Matplotlib Canvas Panel
class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
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
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()
        self.SwapBuffers()

    def InitGL(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)  # Black background
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)

        # Draw a simple cube
        glBegin(GL_QUADS)
        glColor3f(1, 0, 0)  # Red color
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)

        glColor3f(0, 1, 0)  # Green color
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, -1, -1)

        # Additional cube faces...
        glEnd()

# Main Application Class
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='wxPython with Matplotlib and OpenGL')

        splitter = wx.SplitterWindow(frame)
        panel1 = CanvasPanel(splitter)
        panel1.draw()

        openGLcanvas = MyCanvasBase(splitter)

        splitter.SplitVertically(panel1, openGLcanvas, sashPosition=400)
        splitter.SetMinimumPaneSize(100)
        splitter.SetSashPosition(400)

        frame.SetSize(800, 400)
        frame.Show(True)
        return True

app = MyApp()
app.MainLoop()
