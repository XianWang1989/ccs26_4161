
import wx
import sys
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLUT import *
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

# Matplotlib Canvas for plotting
class MatplotlibCanvas(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.draw()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(sizer)

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()

# OpenGL Canvas for rendering shapes
class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = glcanvas.GLContext(self)

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnEraseBackground(self, event):
        pass

    def OnSize(self, event):
        self.Refresh()

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()

    def InitGL(self):
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1, 0.1, 50)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -5)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.DrawCube()
        self.SwapBuffers()

    def DrawCube(self):
        glBegin(GL_QUADS)
        # Define vertices for a cube
        vertices = [(1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, -1),
                    (1, -1, 1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1)]
        edges = [(0, 1), (1, 2), (2, 3), (3, 0),
                 (4, 5), (5, 6), (6, 7), (7, 4),
                 (0, 5), (1, 6), (2, 7), (3, 4)]
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Matplotlib and OpenGL', size=(800, 400))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create and add Matplotlib and OpenGL canvases
        self.matplotlib_canvas = MatplotlibCanvas(panel)
        self.opengl_canvas = MyCanvasBase(panel)

        sizer.Add(self.matplotlib_canvas, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.opengl_canvas, 1, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(sizer)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame()
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
