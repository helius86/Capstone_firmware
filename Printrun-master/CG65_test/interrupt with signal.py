import wx

app = wx.App()

frame = wx.Frame(None, title='Example')
button = wx.Button(frame, label='Restart')

a = 0
flag = 0

def on_button_click(event):
    global a
    global flag
    print('Button clicked')
    if a == 0:
        print('a is', a)
        a = 1
        flag = 1
    print('at end of click: a is', a, flag)

def restartMainLoop():
    app.ExitMainLoop()
    app.MainLoop()

button.Bind(wx.EVT_BUTTON, on_button_click)

def timer_handler(event):
    global flag
    if flag == 1:
        print('flag is 1, interrupting...')
        global a
        a = 0
        flag = 0
        restartMainLoop()

timer = wx.Timer(frame)
frame.Bind(wx.EVT_TIMER, timer_handler, timer)
timer.Start(100) # Run the timer_handler function every 1000 milliseconds (1 second)

frame.Show()
app.MainLoop()
