
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import wx
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *

class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Create a sizer for layout
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create matplotlib canvas
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)

        # Create OpenGL canvas
        self.opengl_canvas = CubeCanvas(self)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND)

        self.SetSizer(self.sizer)
        self.Fit()
        self.draw_plot()

    def draw_plot(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()

class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.context = glcanvas.GLContext(self)
        self.init = False
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnSize(self, event):
        self.Refresh() # Refresh the canvas when resized
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
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1.0, 1.0, -1.0, 1.0, 1.0, 10.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)

class CubeCanvas(MyCanvasBase):
    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glBegin(GL_QUADS)
        # Draw a simple cube
        for face in [(-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), 
                      (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5)]:
            glVertex3f(*face)
        glEnd()

        self.SwapBuffers()

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='Matplotlib and OpenGL in wxPython')
        panel = CanvasPanel(frame)
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
