# -*- coding: utf-8 -*-
import wx

class TestFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,200))

        # define splitter window in our main Frame and
        # put two panels there
        self.sp = wx.SplitterWindow(self)
        self.p1 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        self.p2 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        self.sp.SplitVertically(self.p1, self.p2, 50)

        # define status bar
        self.sb = self.CreateStatusBar()
        self.sb.SetStatusText("Hola!")

        #text = wx.StaticText(self, label="Hello, World!")

app = wx.App(redirect=False)
frame = TestFrame(None, "Hello, world!")
frame.Show()
app.MainLoop()
