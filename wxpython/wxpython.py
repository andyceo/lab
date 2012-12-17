# -*- coding: utf-8 -*-
import wx

class Window(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (300,250))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.Show(True)

        menu = wx.Menu() # создаём экземпляр меню
        openItem = menu.Append(wx.ID_ANY, "Open", "Push the button to open the file")
        aboutItem = menu.Append(wx.ID_ABOUT,"About","Push the button to get an information about this application") # добавляем подпункты к меню
        exitItem = menu.Append(wx.ID_EXIT,"Exit","Push the button to leave this application") # а как ещё?
        bar = wx.MenuBar() # создаём рабочую область для меню
        bar.Append(menu,"File") # добавляем пункт меню
        self.SetMenuBar(bar) # указываем, что это меню надо показать в нашей форме

        self.Bind(wx.EVT_MENU, self.OnOpen, openItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)

    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "This is a mini editor keeping your text","About pyNote", wx.OK) # создаём всплывашку
        dlg.ShowModal() # показываем окошко

    def OnOpen(self, e):
        self.dirname = " "
        openDlg = wx.FileDialog(self, "Choose a file to open", self.dirname, " ", "*.*", wx.OPEN) # создаём диалог
        if openDlg.ShowModal() == wx.ID_OK: # при выборе файла
                self.filename = openDlg.GetFilename() # ловим название файла
                self.dirname = openDlg.GetDirectory() # и папку, в которой он находится
                f = open(os.path.join(self.dirname,self.filename), "r") # открываем файл
                self.control.SetValue(f.read()) # отображаем в текстовом поле
                f.close()
                wnd.SetTitle(self.filename + " - pyNote") # меняем заголовок окна

    def OnExit(self, e):
        self.control.SetValue("Close me, please! :(")

app = wx.App()
wnd = Window(None, "pyNote")
app.MainLoop()
