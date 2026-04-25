
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
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)

        # Sizer for the layout
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.gl_canvas = CubeCanvas(self)  # Add OpenGL Canvas
        self.sizer.Add(self.gl_canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        self.draw_plot()

    def draw_plot(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()

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
            self.init_gl()
            self.init = True

        self.OnDraw()

    def init_gl(self):
        glEnable(GL_DEPTH_TEST)
        glViewport(0, 0, self.GetSize().width, self.GetSize().height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-1, 1, -1, 1, -1, 1)
        glMatrixMode(GL_MODELVIEW)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)  # Move back to see the cube
        self.draw_cube()
        self.SwapBuffers()

    def draw_cube(self):
        glBegin(GL_QUADS)
        # Front face
        glColor3f(1, 0, 0)  # Red
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f(0.5, -0.5, 0.5)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        # Other faces...
        glEnd()

class CubeCanvas(MyCanvasBase):
    def draw_cube(self):
        super().draw_cube()  # Call base implementation

class MyApp(wx.App):
    def OnInit(self):
        self.frame = wx.Frame(None, title='Matplotlib and OpenGL in wxPython', size=(800, 600))
        self.panel = CanvasPanel(self.frame)
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
