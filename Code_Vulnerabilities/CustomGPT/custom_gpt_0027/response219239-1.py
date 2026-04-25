
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

        # Create matplotlib canvas
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)

        # Create OpenGL canvas
        self.gl_canvas = CubeCanvas(self)

        # Layout
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.sizer.Add(self.gl_canvas, 1, wx.EXPAND)

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
        self.init = False
        self.context = glcanvas.GLContext(self)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()

class CubeCanvas(MyCanvasBase):
    def InitGL(self):
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)

        glBegin(GL_QUADS)
        # Draw a simple cube
        for color, vertices in self.get_cube_faces():
            glColor3fv(color)
            for vertex in vertices:
                glVertex3fv(vertex)
        glEnd()

        self.SwapBuffers()

    def get_cube_faces(self):
        return [
            ([1, 0, 0], [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)]),  # Front face
            ([0, 1, 0], [(-1, -1, -1), (-1, 1, -1), (1, 1, -1), (1, -1, -1)]),  # Back face
            ([0, 0, 1], [(-1, 1, -1), (-1, 1, 1), (1, 1, 1), (1, 1, -1)]),  # Top face
            ([1, 1, 0], [(-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1)]),  # Bottom face
            ([1, 0, 1], [(-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1)]),  # Left face
            ([0, 1, 1], [(1, -1, -1), (1, -1, 1), (1, 1, 1), (1, 1, -1)])   # Right face
        ]

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='wxPython + Matplotlib + OpenGL', size=(800, 600))
        panel = CanvasPanel(frame)
        frame.Show()
        return True

app = MyApp()
app.MainLoop()
