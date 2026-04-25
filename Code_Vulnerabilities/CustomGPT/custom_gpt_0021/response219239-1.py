
import wx
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from wx import glcanvas
from OpenGL.GL import *

# Matplotlib Canvas
class MatplotlibPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.draw()  # Initial drawing
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)

# OpenGL Canvas
class OpenGLCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.context = glcanvas.GLContext(self)
        self.init = False
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def on_paint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.init_gl()
            self.init = True
        self.render()
        self.SwapBuffers()

    def init_gl(self):
        glEnable(GL_DEPTH_TEST)

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslate(0.0, 0.0, -5)

        # Drawing a cube
        glBegin(GL_QUADS)
        # Front face
        glColor3f(1.0, 0.0, 0.0)  # Red
        glVertex3f( 1,  1,  1)
        glVertex3f(-1,  1,  1)
        glVertex3f(-1, -1,  1)
        glVertex3f( 1, -1,  1)
        # Back face
        glColor3f(0.0, 1.0, 0.0)  # Green
        glVertex3f(-1, -1, -1)
        glVertex3f(-1,  1, -1)
        glVertex3f( 1,  1, -1)
        glVertex3f( 1, -1, -1)
        glEnd()

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='wxPython, Matplotlib, OpenGL', size=(800, 400))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create and add Matplotlib panel
        mat_panel = MatplotlibPanel(panel)
        sizer.Add(mat_panel, 1, wx.EXPAND)

        # Create and add OpenGL canvas
        opengl_canvas = OpenGLCanvas(panel)
        sizer.Add(opengl_canvas, 1, wx.EXPAND)

        panel.SetSizer(sizer)
        self.Show()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
