
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

import wx
from wx import glcanvas
from OpenGL.GL import *

class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Create a horizontal box sizer
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        # Matplotlib Canvas
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.draw_plot()
        hbox.Add(self.canvas, 1, wx.EXPAND | wx.ALL, 5)

        # OpenGL Canvas
        self.opengl_canvas = CubeCanvas(self)
        hbox.Add(self.opengl_canvas, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(hbox)
        self.Fit()

    def draw_plot(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)

class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = glcanvas.GLContext(self)

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnEraseBackground(self, event):
        pass  # Do nothing to prevent flicker

    def OnSize(self, event):
        wx.CallAfter(self.DoSetViewport)
        event.Skip()

    def DoSetViewport(self):
        size = self.GetClientSize()
        self.SetCurrent(self.context)
        glViewport(0, 0, size.width, size.height)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()

class CubeCanvas(MyCanvasBase):
    def InitGL(self):
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1.0, 1.0, -1.0, 1.0, 1.0, 10.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Drawing a cube
        glBegin(GL_QUADS)
        colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0)]
        vertices = [
            [0.5, 0.5, 0.5], [-0.5, 0.5, 0.5], 
            [-0.5, -0.5, 0.5], [0.5, -0.5, 0.5], 
            [-0.5, -0.5, -0.5], [-0.5, 0.5, -0.5], 
            [0.5, 0.5, -0.5], [0.5, -0.5, -0.5]
        ]

        # Front face
        for i in range(4):
            glColor3f(*colors[i])
            glVertex3f(*vertices[i])

        # Back face
        for i in range(4, 8):
            glColor3f(*colors[(i-4)%4])
            glVertex3f(*vertices[i])
        glEnd()

        self.SwapBuffers()

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='Matplotlib and OpenGL Canvas', size=(800, 600))
        panel = CanvasPanel(frame)
        frame.Show(True)
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
