
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import wx
import wx.glcanvas as glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *

# Matplotlib Canvas
class PlotCanvas(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()
        self.draw()

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()

# OpenGL Canvas
class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = glcanvas.GLContext(self)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)

    def on_paint(self, event):
        self.SetCurrent(self.context)
        if not self.init:
            self.init_gl()
            self.init = True
        self.on_draw()

    def on_size(self, event):
        self.SetCurrent(self.context)
        size = self.GetClientSize()
        glViewport(0, 0, size.width, size.height)
        event.Skip()

    def init_gl(self):
        glClearColor(0.1, 0.1, 0.1, 1)
        glEnable(GL_DEPTH_TEST)

    def on_draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5)
        glBegin(GL_QUADS)
        glColor3f(1, 0, 0)
        glVertex3f(-1, -1, 0)
        glVertex3f(1, -1, 0)
        glVertex3f(1, 1, 0)
        glVertex3f(-1, 1, 0)
        glEnd()
        self.SwapBuffers()

# Main Application
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='Matplotlib and OpenGL Example', size=(800, 600))
        panel = wx.Panel(frame)

        # Create a horizontal sizer
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create the matplotlib canvas
        plot_canvas = PlotCanvas(panel)
        sizer.Add(plot_canvas, 1, wx.EXPAND)

        # Create the OpenGL canvas
        opengl_canvas = MyCanvasBase(panel)
        sizer.Add(opengl_canvas, 1, wx.EXPAND)

        panel.SetSizer(sizer)
        frame.Show()
        return True

# Run the application
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
