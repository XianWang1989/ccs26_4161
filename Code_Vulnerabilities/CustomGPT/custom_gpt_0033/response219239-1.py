
import wx
import wx.glcanvas as glcanvas
from OpenGL.GL import *
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Create sizer for layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add Matplotlib canvas
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.draw_plot()
        sizer.Add(self.canvas, 1, wx.EXPAND)

        # Add OpenGL canvas
        self.opengl_canvas = CubeCanvas(self)
        sizer.Add(self.opengl_canvas, 1, wx.EXPAND)

        self.SetSizer(sizer)
        self.Fit()

    def draw_plot(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)

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
            self.InitGL()
            self.init = True
        self.OnDraw()

class CubeCanvas(MyCanvasBase):
    def InitGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        self.draw_cube()
        self.SwapBuffers()

    def draw_cube(self):
        glBegin(GL_QUADS)
        # Front face
        glColor3f(1, 0, 0)
        glVertex3f(-1, -1, 1)
        glVertex3f( 1, -1, 1)
        glVertex3f( 1,  1, 1)
        glVertex3f(-1,  1, 1)
        # Back face
        glColor3f(0, 1, 0)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1,  1, -1)
        glVertex3f( 1,  1, -1)
        glVertex3f( 1, -1, -1)
        # other faces...
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
