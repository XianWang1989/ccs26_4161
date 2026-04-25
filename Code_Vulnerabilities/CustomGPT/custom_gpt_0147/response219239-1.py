
import wx
import wx.glcanvas as glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *
import matplotlib
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

matplotlib.use('WXAgg')

class MatplotlibCanvas(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        self.draw()

    def draw(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()


class OpenGLCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.context = glcanvas.GLContext(self)
        self.init = False
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def initGL(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, 1.0, 1.0, 100.0)
        glTranslatef(0.0, 0.0, -5)

    def on_paint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.initGL()
            self.init = True
        self.on_draw()
        self.SwapBuffers()

    def on_draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_QUADS)
        # Define vertices for a simple cube (similar to previous code)
        glColor3f(1, 0, 0)
        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(-1, 1, -1)
        glEnd()


class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)

        # Create a panel that holds both canvases
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create Matplotlib canvas
        self.matplotlib_canvas = MatplotlibCanvas(panel)
        sizer.Add(self.matplotlib_canvas, 1, wx.EXPAND)

        # Create OpenGL canvas
        self.opengl_canvas = OpenGLCanvas(panel)
        sizer.Add(self.opengl_canvas, 1, wx.EXPAND)

        panel.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame(None, title='Matplotlib and OpenGL Canvas')
    frame.Show()
    app.MainLoop()
