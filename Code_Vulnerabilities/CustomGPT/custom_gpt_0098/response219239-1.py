
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

        # Create sizer to organize layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create Matplotlib canvas
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer_matplotlib = wx.BoxSizer(wx.VERTICAL)
        self.sizer_matplotlib.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(sizer)
        sizer.Add(self.sizer_matplotlib, 1, wx.EXPAND)

        # Create OpenGL canvas
        self.opengl_canvas = CubeCanvas(self)
        sizer.Add(self.opengl_canvas, 1, wx.EXPAND)

        # Draw the plot on the Matplotlib canvas
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

        # Event bindings
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnEraseBackground(self, event):
        pass  # Prevent flashing

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

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)  # Move back

        # Draw a cube
        glBegin(GL_QUADS)
        for color, vertices in zip([(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0)], [
            [(1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1)],  # Front face
            [(1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1)],  # Back face
            [(1, 1, 1), (1, 1, -1), (-1, 1, -1), (-1, 1, 1)],  # Top face
            [(1, -1, -1), (-1, -1, -1), (-1, -1, 1), (1, -1, 1)],  # Bottom face
        ]):
            glColor3fv(color)
            for vertex in vertices:
                glVertex3fv(vertex)
        glEnd()

        self.SwapBuffers()


class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='Combined Canvas Example', size=(800, 400))
        panel = CanvasPanel(frame)
        frame.Show()
        return True

app = MyApp()
app.MainLoop()
