#!/usr/bin/env python3

# This file is part of the Printrun suite.
#
# Printrun is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Printrun is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Printrun.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import getopt

# 代码的第一部分检查是否安装了所需版本的 wxPython 库，如果没有，则引发错误消息。
try:
    import wx  # NOQA
    if wx.VERSION < (4,):
        raise ImportError()
except:
    print("wxPython >= 4 is not installed. This program requires wxPython >=4 to run.")
    raise

# include the PronterApp class from the "pronterface" module of the "printrun" package
from printrun.pronterface import PronterApp
from printcore import printcore

flag = 0



# 在“main”块中，脚本使用 getopt 库来处理命令行选项和参数。
# 选项包括打印帮助消息、打印程序版本号、增加详细程度、启动时自动连接打印机、
# 指定启动时加载的配置文件以及加载配置后执行命令。
if __name__ == '__main__':

    from printrun.printcore import __version__ as printcore_version

    os.environ['GDK_BACKEND'] = 'x11'

    usage = "Usage:\n"+\
            "  pronterface [OPTIONS] [FILE]\n\n"+\
            "Options:\n"+\
            "  -h, --help\t\t\tPrint this help message and exit\n"+\
            "  -V, --version\t\t\tPrint program's version number and exit\n"+\
            "  -v, --verbose\t\t\tIncrease verbosity\n"+\
            "  -a, --autoconnect\t\tAutomatically try to connect to printer on startup\n"+\
            "  -c, --conf, --config=CONFIG_FILE\tLoad this file on startup instead of .pronsolerc; you may chain config files, if so settings auto-save will use the last specified file\n"+\
            "  -e, --execute=COMMAND\t\tExecutes command after configuration/.pronsolerc is loaded; macros/settings from these commands are not autosaved"

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hVvac:e:", ["help", "version", "verbose", "autoconnect", "conf=", "config=", "execute="])
    except getopt.GetoptError as err:
        print(str(err))
        print(usage)
        sys.exit(2)
    for o, a in opts:
        if o in ('-V','--version'):
            print("printrun "+printcore_version)
            sys.exit(0)
        elif o in ('-h', '--help'):
            print(usage)
            sys.exit(0)

# 最后，脚本创建 PronterApp 类的实例，
# 并调用其 MainLoop() 方法启动主应用程序循环。 
# MainLoop() 方法为用户界面提供事件处理和控制 3D 打印机的逻辑。
    app = PronterApp(False) 
    opCore = printcore()
    # 这里PronterApp是一个class，创建一个app变量，并将PronterApp实例化，传递参数为False
    # 具体PronterApp内部定义了哪些def功能，得去看PronterApp是怎么定义的





    def restartMainLoop():
        app.ExitMainLoop()
        app.MainLoop()

    def timer_handler(event):
        opCore.send_now("M114")
        # global flag
        # if flag == 1:
        #     print('flag is 1, interrupting...')
        #     a = 0
        #     flag = 0
        #     restartMainLoop()

    timer = wx.Timer(app)
    app.Bind(wx.EVT_TIMER, timer_handler, timer)
    timer.Start(10000) # Run the timer_handler function every 1000 milliseconds (1 second)


    try:
        app.MainLoop()
    except KeyboardInterrupt:
        pass
    del app

# 此脚本提供 Pronterface 的主要功能，并允许用户使用图形用户界面控制 3D 打印机并与之通信。





