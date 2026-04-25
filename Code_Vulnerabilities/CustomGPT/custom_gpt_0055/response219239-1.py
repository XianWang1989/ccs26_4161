
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

        # Draw the matplotlib graph
        self.draw()

    def draw(self):
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
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()
        self.SwapBuffers()

    def InitGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)

        # Drawing a cube
        glBegin(GL_QUADS)
        for face in [((1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1)),  # Front face
                     ((-1, -1, -1), (-1, 1, -1), (1, 1, -1), (1, -1, -1)),  # Back face
                     ((1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1)),  # Right face
                     ((-1, -1, -1), (-1, -1, 1), (-1, 1, 1), (-1, 1, -1)),  # Left face
                     ((-1, 1, 1), (1, 1, 1), (1, 1, -1), (-1, 1, -1)),  # Top face
                     ((-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1))]:  # Bottom face
            for vertex in face:
                glVertex3f(*vertex)
        glEnd()


class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='Matplotlib and OpenGL Example')
        panel = CanvasPanel(frame)
        frame.SetSize(800, 600)
        frame.Show()
        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
