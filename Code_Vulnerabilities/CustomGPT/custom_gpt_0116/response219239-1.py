
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
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)  # Use horizontal sizer for side-by-side
        self.sizer.Add(self.canvas, 1, wx.EXPAND)

        # OpenGL canvas
        self.opengl_canvas = CubeCanvas(self)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND)

        self.SetSizer(self.sizer)
        self.Fit()

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.axes.set_title('Sine Wave')
        self.canvas.draw()

class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = glcanvas.GLContext(self)
        self.size = None
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnEraseBackground(self, event):
        pass  # Do nothing, to avoid flashing on MSW.

    def OnSize(self, event):
        size = self.GetClientSize()
        self.SetCurrent(self.context)
        glViewport(0, 0, size.width, size.height)
        event.Skip()

    def OnPaint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()
        self.SwapBuffers()

class CubeCanvas(MyCanvasBase):
    def InitGL(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1.0, 1.0, -1.0, 1.0, 1.0, 10.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        glRotatef(30, 1, 0, 0)
        glRotatef(30, 0, 1, 0)

        # Draw cube
        glBegin(GL_QUADS)
        for color, vertices in zip([(1,0,0), (0,1,0), (0,0,1)], [
            [( 0.5,  0.5,  0.5), (0.5,  0.5, -0.5), (-0.5,  0.5, -0.5), (-0.5,  0.5,  0.5)],
            [( 0.5, -0.5, -0.5), (0.5, -0.5,  0.5), (-0.5, -0.5,  0.5), (-0.5, -0.5, -0.5)],
            [( 0.5,  0.5,  0.5), (0.5,  0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5,  0.5)],
        ]):
            glColor3fv(color)
            for vertex in vertices:
                glVertex3fv(vertex)
        glEnd()

class RunDemoApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='Matplotlib with OpenGL in wxPython', size=(800, 600))
        panel = CanvasPanel(frame)
        panel.draw()
        frame.Show()
        return True

if __name__ == "__main__":
    app = RunDemoApp()
    app.MainLoop()
