import wx
a = 0
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        
        wx.Frame.__init__(self, parent, title=title, size=(200, 100))
        self.counter = 0
        #self.Bind(wx.EVT_BUTTON, self.on_button_click)
        self.Bind(wx.EVT_BUTTON, self.on_button_click)
        self.Bind(wx.EVT_CLOSE, self.on_close)
        
        panel = wx.Panel(self)
        button = wx.Button(panel, label="Click Me")
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(button, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)
        
    def on_button_click(self, event):
        global a
        if(a == 0):
            self.counter += 1
            a = 1
        else:
            self.counter -= 1
            a = 0
        print("Button clicked", self.counter, "times")
        
    def on_close(self, event):
        self.Destroy()
        
# 这里就类似于: class PronterApp(wx.App)
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, "Sample Frame")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True
    
app = MyApp()
app.MainLoop()
