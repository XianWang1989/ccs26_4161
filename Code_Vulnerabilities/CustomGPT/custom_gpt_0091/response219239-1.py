
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

        # Create sizer for layout
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create Matplotlib canvas
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)

        # Create the widget to display the matplotlib figure
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer.Add(self.canvas, 1, wx.EXPAND | wx.ALL, 5)

        # Create OpenGL canvas
        self.opengl_canvas = CubeCanvas(self)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(self.sizer)
        self.Fit()

        self.draw_matplotlib()

    def draw_matplotlib(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()


class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = glcanvas.GLContext(self)

        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

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
        glMatrixMode(GL_PROJECTION)
        glFrustum(-1.0, 1.0, -1.0, 1.0, 1.0, 10.0)
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(0.0, 0.0, -5.0)
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glRotatef(30, 1.0, 1.0, 0.0)  # Rotate cube
        self.draw_cube()
        self.SwapBuffers()

    def draw_cube(self):
        # Draw a cube
        glBegin(GL_QUADS)
        for color, coords in [
            ((1, 0, 0), [(1, 1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1)]),  # Front Red
            ((0, 1, 0), [(1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1)]),  # Back Green
            ((0, 0, 1), [(1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1)]),  # Right Blue
            ((1, 1, 0), [(-1, -1, -1), (-1, -1, 1), (-1, 1, 1), (-1, 1, -1)]),  # Left Yellow
            ((1, 0, 1), [(1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1)]),  # Top Magenta
            ((0, 1, 1), [(1, -1, -1), (-1, -1, -1), (-1, -1, 1), (1, -1, 1)])  # Bottom Cyan
        ]:
            glColor3f(*color)
            for x, y, z in coords:
                glVertex3f(x, y, z)
        glEnd()


class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='Matplotlib and OpenGL in wxPython', size=(800, 600))
        panel = CanvasPanel(frame)
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
