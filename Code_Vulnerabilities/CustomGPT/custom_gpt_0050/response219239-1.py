
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import wx
from wx import glcanvas
from OpenGL.GL import *

# Matplotlib canvas class
class MatplotlibCanvas(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()

# OpenGL canvas class
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
        self.SwapBuffers()

    def InitGL(self):
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        glRotatef(30, 1, 0, 0)
        glRotatef(30, 0, 1, 0)

        # Draw cube
        glBegin(GL_QUADS)
        # Front face
        glColor3f(1, 0, 0)  # red
        glVertex3f(-1, -1,  1)
        glVertex3f( 1, -1,  1)
        glVertex3f( 1,  1,  1)
        glVertex3f(-1,  1,  1)
        # Add other faces ...
        glEnd()

# Main application class
class MyApp(wx.App):
    def OnInit(self):
        self.frame = wx.Frame(None, title='Matplotlib and OpenGL', size=(800, 600))

        # Create main sizer
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create Matplotlib and OpenGL canvases
        matplotlib_canvas = MatplotlibCanvas(self.frame)
        openGL_canvas = MyCanvasBase(self.frame)

        # Add canvases to sizer
        main_sizer.Add(matplotlib_canvas, 1, wx.EXPAND)
        main_sizer.Add(openGL_canvas, 1, wx.EXPAND)

        self.frame.SetSizer(main_sizer)
        self.frame.Show()

        # Draw the Matplotlib graph
        matplotlib_canvas.draw()

        return True

# Run the application
if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
