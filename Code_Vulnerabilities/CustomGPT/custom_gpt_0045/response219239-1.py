
import wx
import sys
from wx import glcanvas
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

# Matplotlib Canvas
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

        self.draw()

    def draw(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)
        self.canvas.draw()

# OpenGL Canvas
class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.init = False
        self.context = glcanvas.GLContext(self)

        self.lastx, self.lasty = 30, 30
        self.size = None
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)

    def OnEraseBackground(self, event):
        pass  # Do nothing, to avoid flashing on MSW.

    def OnSize(self, event):
        wx.CallAfter(self.DoSetViewport)
        event.Skip()

    def DoSetViewport(self):
        size = self.size = self.GetClientSize()
        self.SetCurrent(self.context)
        glViewport(0, 0, size.width, size.height)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()

    def OnMouseDown(self, evt):
        self.CaptureMouse()
        self.lastx, self.lasty = evt.GetPosition()

    def OnMouseUp(self, evt):
        self.ReleaseMouse()

    def OnMouseMotion(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            x, y = evt.GetPosition()
            self.lastx, self.lasty = x, y
            self.Refresh(False)

class CubeCanvas(MyCanvasBase):
    def InitGL(self):
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, 1.0, 1.0, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        glEnable(GL_DEPTH_TEST)

    def OnDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glRotatef(25, 1, 0, 0)
        glRotatef(25, 0, 1, 0)

        # Draw a cube
        glBegin(GL_QUADS)
        for color in [(1,0,0), (0,1,0), (0,0,1), (1,1,0), (1,0,1), (0,1,1)]:
            glColor3f(*color)
            glVertex3f(1, 1, 1)
            glVertex3f(-1, 1, 1)
            glVertex3f(-1, -1, 1)
            glVertex3f(1, -1, 1)
        glEnd()

        self.SwapBuffers()

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Matplotlib and OpenGL Example', size=(800, 600))
        panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.matplotlib_canvas = MatplotlibCanvas(panel)
        self.opengl_canvas = CubeCanvas(panel)

        self.sizer.Add(self.matplotlib_canvas, 1, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.opengl_canvas, 1, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(self.sizer)
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
