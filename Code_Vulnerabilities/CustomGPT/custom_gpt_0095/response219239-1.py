
import wx
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *

# Matplotlib Canvas
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

# OpenGL Canvas
class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = glcanvas.GLContext(self)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnEraseBackground(self, event):
        pass  # Do nothing to avoid flashing

    def OnSize(self, event):
        self.SetCurrent(self.context)
        glViewport(0, 0, self.GetClientSize().width, self.GetClientSize().height)
        event.Skip()

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
        for color, vertices in [((1, 0, 0), [(1, 1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1)]),
                                 ((0, 1, 0), [(-1, -1, -1), (-1, 1, -1), (1, 1, -1), (1, -1, -1)])]:
            glColor3f(*color)
            for vertex in vertices:
                glVertex3f(*vertex)
        glEnd()
        self.SwapBuffers()

# Main Application
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, -1, 'Matplotlib + OpenGL', size=(800, 400))
        panel = wx.Panel(frame)

        # Create sizer
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add Matplotlib canvas
        self.matplotlib_panel = CanvasPanel(panel)
        self.matplotlib_panel.draw()
        sizer.Add(self.matplotlib_panel, 1, wx.EXPAND | wx.ALL, 5)

        # Add OpenGL canvas
        self.opengl_canvas = MyCanvasBase(panel)
        sizer.Add(self.opengl_canvas, 1, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(sizer)
        frame.Show()
        return True

app = MyApp()
app.MainLoop()
