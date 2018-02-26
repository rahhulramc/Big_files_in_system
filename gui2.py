import wx,wx.html
import os
import sys
from getsize import *

ar=[("",0)]
answer=[]
banswer=[]
class newwindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "File List",size=(800,500))
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)
        
        self.list = wx.ListCtrl(panel, -1, style = wx.LC_REPORT) 
        self.list.InsertColumn(0, 'Path', width = 600) 
        self.list.InsertColumn(1, 'Size(MB)', wx.LIST_FORMAT_RIGHT, 100)
        j=0
        for i in answer: 
            index=self.list.InsertStringItem(sys.maxint, answer[j]) 
            self.list.SetStringItem(index,1,banswer[j])
            j+=1  
            
        box.Add(self.list,1,wx.EXPAND) 
        panel.SetSizer(box) 
        panel.Fit() 
        self.Centre() 
        self.Show(True)  

class myframe(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Infrastructure",size=(400,300))
        self.panel = wx.Panel(self)
        self.text = wx.TextCtrl(self.panel, -1, pos = (10,10), size=(300,-1))
        self.button_open = wx.Button(self.panel, label = "Open", pos=(310,10), size = (80,-1))
        self.buttongetsize = wx.Button(self.panel, label = 'GetSize', pos=(150,40), size=(70, -1))
        self.Bind(wx.EVT_BUTTON, self.fopen, self.button_open)
        dirname = os.environ['HOME']
        self.text.SetValue(dirname)
        self.Bind(wx.EVT_BUTTON,self.gsize,self.buttongetsize)
        
    def fopen(self,event):
        style=wx.OPEN
        fdialog=wx.DirDialog(self,'Open',style=style)
        if fdialog.ShowModal()==wx.ID_OK:
            self.path=fdialog.GetPath()
            self.text.SetValue(self.path)
    def gsize(self,event):
        l = self.text.GetValue()
        l=l+"/"
        ar=gts(l)
        j=0
        for i in ar:
            answer.append(i[0])
            banswer.append(unicode((str((float)(i[1])/(float)(1000*1000))),"utf-8"))
        print banswer
        dlg = newwindow()
        dlg.Show()

if __name__=='__main__':
    app = wx.PySimpleApp()
    frame = myframe(None, -1)
    frame.Show()
    app.MainLoop()