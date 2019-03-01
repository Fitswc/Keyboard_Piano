from easygui import *
from main import *

def lan():
    a = buttonbox(msg='Keyboard Piano',title='Keyboard Piano',choices=('启动','操作说明/关于'))
    if a == '启动':
        main()

    if a == '操作说明/关于':
        textbox(msg='操作说明/关于', title='Reader', text='KeyboardPiano 操作说明/关于\n\n按下:1,2,3,4,5,6,7,8 发出声音\n本钢琴声为C调\n按下键时会有一秒延迟\n\n使用到的工具:\n1. python3.7(64-bit)\n2. pygame\n3. easygui')
        lan()

lan()
