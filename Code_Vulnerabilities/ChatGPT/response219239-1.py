
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
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create matplotlib canvas
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.fig)
        self.draw_matplotlib()

        # Create OpenGL canvas
        self.opengl_canvas = CubeCanvas(self)

        # Add both canvases to the sizer
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND)

        self.SetSizer(self.sizer)

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

        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()
        self.SwapBuffers()

    def InitGL(self):
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)  # Move back

        # Draw a cube
        glBegin(GL_QUADS)
        # Front face
        glColor3f(1, 0, 0); glVertex3f(1, 1, 1)
        glColor3f(0, 1, 0); glVertex3f(-1, 1, 1)
        glColor3f(0, 0, 1); glVertex3f(-1, -1, 1)
        glColor3f(1, 1, 0); glVertex3f(1, -1, 1)
        glEnd()

        # Add other faces here as necessary


class CubeCanvas(MyCanvasBase):
    def OnDraw(self):
        super().OnDraw()
        # You can add extra drawing or transformation methods here


class RunDemoApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='Matplotlib and OpenGL Example', size=(800, 600))
        panel = CanvasPanel(frame)
        frame.Show()
        return True


if __name__ == "__main__":
    app = RunDemoApp()
    app.MainLoop()
