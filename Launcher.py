import easygui as g
from main import *
a = g.buttonbox(msg='Keyboard Piano',title='Keyboard Piano',choices=('启动','操作说明/关于'))
if a == '启动':
    main()

if a == '操作说明/关于':
    msg = '操作说明/关于'
    title = 'reader'
    b = 'key.txt'
    c = g.textbox(msg,title,text = open(b))
    
